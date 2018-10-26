import numpy as np
import tensorflow as tf
from tensorflow.contrib import slim as slim

from yolo.net.layer import Layer
from yolo.net.baseop import BaseOp


class reorg(BaseOp):
    def _forward(self):
        inp = self.inp.out
        shape = inp.get_shape().as_list()
        _, h, w, c = shape
        s = self.lay.stride
        out = list()
        for i in range(int(h/s)):
            row_i = list()
            for j in range(int(w/s)):
                si, sj = s * i, s * j
                boxij = inp[:, si: si+s, sj: sj+s,:]
                flatij = tf.reshape(boxij, [-1,1,1,c*s*s])
                row_i += [flatij]
            out += [tf.concat(row_i, 2)]

        self.out = tf.concat(out, 1)

    def forward(self):
        inp = self.inp.out
        s = self.lay.stride
        self.out = tf.extract_image_patches(
            inp, [1,s,s,1], [1,s,s,1], [1,1,1,1], 'VALID')

    def speak(self):
        args = [self.lay.stride] * 2
        msg = 'local flatten {}x{}'
        return msg.format(*args)


class local(BaseOp):
    def forward(self):
        pad = [[self.lay.pad, self.lay.pad]] * 2;
        temp = tf.pad(self.inp.out, [[0, 0]] + pad + [[0, 0]])

        k = self.lay.w['kernels']
        ksz = self.lay.ksize
        half = int(ksz / 2)
        out = list()
        for i in range(self.lay.h_out):
            row_i = list()
            for j in range(self.lay.w_out):
                kij = k[i * self.lay.w_out + j]
                i_, j_ = i + 1 - half, j + 1 - half
                tij = temp[:, i_ : i_ + ksz, j_ : j_ + ksz,:]
                row_i.append(
                    tf.nn.conv2d(tij, kij,
                        padding = 'VALID',
                        strides = [1] * 4))
            out += [tf.concat(row_i, 2)]

        self.out = tf.concat(out, 1)

    def speak(self):
        l = self.lay
        args = [l.ksize] * 2 + [l.pad] + [l.stride]
        args += [l.activation]
        msg = 'loca {}x{}p{}_{}  {}'.format(*args)
        return msg


class convolutional(BaseOp):
    def forward(self):
        pad = [[self.lay.pad, self.lay.pad]] * 2;
        temp = tf.pad(self.inp.out, [[0, 0]] + pad + [[0, 0]])
        temp = tf.nn.conv2d(temp, self.lay.w['kernel'], padding = 'VALID',
            name = self.scope, strides = [1] + [self.lay.stride] * 2 + [1])
        if self.lay.batch_norm:
            temp = self.batchnorm(self.lay, temp)
        self.out = tf.nn.bias_add(temp, self.lay.w['biases'])

    def batchnorm(self, layer, inp):
        if not self.var:
            temp = (inp - layer.w['moving_mean'])
            temp /= (np.sqrt(layer.w['moving_variance']) + 1e-5)
            temp *= layer.w['gamma']
            return temp
        else:
            args = dict({
                'center' : False, 'scale' : True,
                'epsilon': 1e-5, 'scope' : self.scope,
                'updates_collections' : None,
                'is_training': layer.h['is_training'],
                'param_initializers': layer.w
                })
            return slim.batch_norm(inp, **args)

    def speak(self):
        l = self.lay
        args = [l.ksize] * 2 + [l.pad] + [l.stride]
        args += [l.batch_norm * '+bnorm']
        args += [l.activation]
        msg = 'conv {}x{}p{}_{}  {}  {}'.format(*args)
        return msg


class conv_select(convolutional):
    def speak(self):
        l = self.lay
        args = [l.ksize] * 2 + [l.pad] + [l.stride]
        args += [l.batch_norm * '+bnorm']
        args += [l.activation]
        msg = 'sele {}x{}p{}_{}  {}  {}'.format(*args)
        return msg


class conv_extract(convolutional):
    def speak(self):
        l = self.lay
        args = [l.ksize] * 2 + [l.pad] + [l.stride]
        args += [l.batch_norm * '+bnorm']
        args += [l.activation]
        msg = 'extr {}x{}p{}_{}  {}  {}'.format(*args)
        return msg


class local_layer(Layer):
    def setup(self, ksize, c, n, stride,
              pad, w_, h_, activation):
        self.pad = pad * int(ksize / 2)
        self.activation = activation
        self.stride = stride
        self.ksize = ksize
        self.h_out = h_
        self.w_out = w_

        self.dnshape = [h_ * w_, n, c, ksize, ksize]
        self.wshape = dict({
            'biases': [h_ * w_ * n],
            'kernels': [h_ * w_, ksize, ksize, c, n]
        })

    def finalize(self, _):
        weights = self.w['kernels']
        if weights is None: return
        weights = weights.reshape(self.dnshape)
        weights = weights.transpose([0,3,4,2,1])
        self.w['kernels'] = weights


class conv_extract_layer(Layer):
    def setup(self, ksize, c, n, stride,
              pad, batch_norm, activation,
              inp, out):
        if inp is None: inp = range(c)
        self.activation = activation
        self.batch_norm = batch_norm
        self.stride = stride
        self.ksize = ksize
        self.pad = pad
        self.inp = inp
        self.out = out
        self.wshape = dict({
            'biases': [len(out)],
            'kernel': [ksize, ksize, len(inp), len(out)]
        })

    @property
    def signature(self):
        sig = ['convolutional']
        sig += self._signature[1:-2]
        return sig

    def present(self):
        args = self.signature
        self.presenter = convolutional_layer(*args)

    def recollect(self, w):
        if w is None:
            self.w = w
            return
        k = w['kernel']
        b = w['biases']
        k = np.take(k, self.inp, 2)
        k = np.take(k, self.out, 3)
        b = np.take(b, self.out)
        assert1 = k.shape == tuple(self.wshape['kernel'])
        assert2 = b.shape == tuple(self.wshape['biases'])
        assert assert1 and assert2, \
        'Dimension not matching in {} recollect'.format(
            self._signature)
        self.w['kernel'] = k
        self.w['biases'] = b


class conv_select_layer(Layer):
    def setup(self, ksize, c, n, stride,
              pad, batch_norm, activation,
              keep_idx, real_n):
        self.batch_norm = bool(batch_norm)
        self.activation = activation
        self.keep_idx = keep_idx
        self.stride = stride
        self.ksize = ksize
        self.pad = pad
        self.wshape = dict({
            'biases': [real_n],
            'kernel': [ksize, ksize, c, real_n]
        })
        if self.batch_norm:
            self.wshape.update({
                'moving_variance'  : [real_n],
                'moving_mean': [real_n],
                'gamma' : [real_n]
            })
            self.h['is_training'] = {
                'shape': (),
                'feed': True,
                'dfault': False
            }

    @property
    def signature(self):
        sig = ['convolutional']
        sig += self._signature[1:-2]
        return sig

    def present(self):
        args = self.signature
        self.presenter = convolutional_layer(*args)

    def recollect(self, w):
        if w is None:
            self.w = w
            return
        idx = self.keep_idx
        k = w['kernel']
        b = w['biases']
        self.w['kernel'] = np.take(k, idx, 3)
        self.w['biases'] = np.take(b, idx)
        if self.batch_norm:
            m = w['moving_mean']
            v = w['moving_variance']
            g = w['gamma']
            self.w['moving_mean'] = np.take(m, idx)
            self.w['moving_variance'] = np.take(v, idx)
            self.w['gamma'] = np.take(g, idx)


class convolutional_layer(Layer):
    def setup(self, ksize, c, n, stride,
              pad, batch_norm, activation):
        self.batch_norm = bool(batch_norm)
        self.activation = activation
        self.stride = stride
        self.ksize = ksize
        self.pad = pad
        self.dnshape = [n, c, ksize, ksize] # darknet shape
        self.wshape = dict({
            'biases': [n],
            'kernel': [ksize, ksize, c, n]
        })
        if self.batch_norm:
            self.wshape.update({
                'moving_variance'  : [n],
                'moving_mean': [n],
                'gamma' : [n]
            })
            self.h['is_training'] = {
                'feed': True,
                'dfault': False,
                'shape': ()
            }

    def finalize(self, _):
        """deal with darknet"""
        kernel = self.w['kernel']
        if kernel is None: return
        kernel = kernel.reshape(self.dnshape)
        kernel = kernel.transpose([2,3,1,0])
        self.w['kernel'] = kernel