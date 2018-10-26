from yolo.net.simple import route, connected, select, extract, flatten, softmax, avgpool, dropout, crop, maxpool, leaky, \
	identity
from yolo.net.convolution import reorg, local, convolutional, conv_select, conv_extract

op_types = {
	'convolutional': convolutional,
	'conv-select': conv_select,
	'connected': connected,
	'maxpool': maxpool,
	'leaky': leaky,
	'dropout': dropout,
	'flatten': flatten,
	'avgpool': avgpool,
	'softmax': softmax,
	'identity': identity,
	'crop': crop,
	'local': local,
	'select': select,
	'route': route,
	'reorg': reorg,
	'conv-extract': conv_extract,
	'extract': extract
}


def op_create(*args):
	layer_type = list(args)[0].type
	return op_types[layer_type](*args)