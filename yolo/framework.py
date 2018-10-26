from yolo.models import yolo, vanilla
from darkflow.darkflow.net import yolov2
from os.path import basename

class framework(object):
    constructor = vanilla.constructor
    loss = yolo.models.vanilla.train.loss
    
    def __init__(self, meta, FLAGS):
        model = basename(meta['model'])
        model = '.'.join(model.split('.')[:-1])
        meta['name'] = model
        
        self.constructor(meta, FLAGS)

    def is_inp(self, file_name):
        return True

class YOLO(framework):
    constructor = yolo.moels.constructor
    parse = yolo.models.yolo.data.parse
    shuffle = yolo.models.yolo.data.shuffle
    preprocess = yolo.models.yolo.predict.preprocess
    postprocess = yolo.models.yolo.predict.postprocess
    loss = yolo.models.yolo.train.loss
    is_inp = yolo.misc.is_inp
    profile = yolo.misc.profile
    _batch = yolo.models.yolo.data._batch
    resize_input = yolo.models.yolo.predict.resize_input
    findboxes = yolo.models.yolo.predict.findboxes
    process_box = yolo.models.yolo.predict.process_box

class YOLOv2(framework):
    constructor = yolo.moels.constructor
    parse = yolo.models.yolo.data.parse
    shuffle = yolov2.data.shuffle
    preprocess = yolo.models.yolo.predict.preprocess
    loss = yolov2.train.loss
    is_inp = yolo.misc.is_inp
    postprocess = yolov2.predict.postprocess
    _batch = yolov2.data._batch
    resize_input = yolo.models.yolo.predict.resize_input
    findboxes = yolov2.predict.findboxes
    process_box = yolo.models.yolo.predict.process_box

"""
framework factory
"""

types = {
    '[detection]': YOLO,
    '[region]': YOLOv2
}

def create_framework(meta, FLAGS):
    net_type = meta['type']
    this = types.get(net_type, framework)
    return this(meta, FLAGS)