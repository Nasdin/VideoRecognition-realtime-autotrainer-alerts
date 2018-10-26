from yolo.net.connected import connected_layer, extract_layer, select_layer
from yolo.net.convolution import local_layer, conv_extract_layer, conv_select_layer, convolutional_layer
from yolo.net.layer import Layer


class avgpool_layer(Layer):
    pass


class crop_layer(Layer):
    pass


class maxpool_layer(Layer):
    def setup(self, ksize, stride, pad):
        self.stride = stride
        self.ksize = ksize
        self.pad = pad


class softmax_layer(Layer):
    def setup(self, groups):
        self.groups = groups


class dropout_layer(Layer):
    def setup(self, p):
        self.h['pdrop'] = dict({
            'feed': p, # for training
            'dfault': 1.0, # for testing
            'shape': ()
        })


class route_layer(Layer):
    def setup(self, routes):
        self.routes = routes


class reorg_layer(Layer):
    def setup(self, stride):
        self.stride = stride


darkops = {
    'dropout': dropout_layer,
    'connected': connected_layer,
    'maxpool': maxpool_layer,
    'convolutional': convolutional_layer,
    'avgpool': avgpool_layer,
    'softmax': softmax_layer,
    'crop': crop_layer,
    'local': local_layer,
    'select': select_layer,
    'route': route_layer,
    'reorg': reorg_layer,
    'conv-select': conv_select_layer,
    'conv-extract': conv_extract_layer,
    'extract': extract_layer
}


def create_darkop(ltype, num, *args):
    op_class = darkops.get(ltype, Layer)
    return op_class(ltype, num, *args)