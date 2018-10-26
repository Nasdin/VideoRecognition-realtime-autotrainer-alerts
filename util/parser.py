from util.defaults import argHandler
from config import MODEL_CFG_FILE_PATH, MODEL_WEIGHT
from collections import namedtuple
import os
from darkflow.darkflow.net.build import TFNet

UserRunInput = namedtuple("UserRunInputs",
                          ['use_gpu', 'use_video', 'use_camera', 'video_path', 'save', 'save_video_fp'])
UserTrainInput = namedtuple("UserTrainInputs", ['use_gpu', 'epoch', 'save', 'learning_rate', 'batch'])


class YoloArgs(argHandler):

    def __init__(self, user_inputs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Need to set the model and weight paths
        self['model'] = MODEL_CFG_FILE_PATH
        self['load'] = MODEL_WEIGHT
        self.take_user_inputs(user_inputs)

    def take_user_inputs(self, input_dict: namedtuple):

        if type(input_dict).__name__ == 'UserRunInputs':
            self._parse_run_inputs(input_dict)
        elif type(input_dict).__name__ == "UserTrainInputs":
            self._parse_train_inputs(input_dict)

    def _parse_run_inputs(self, tuple_input: UserRunInput):
        if tuple_input.use_gpu:
            self['gpu'] = 1.0
        if tuple_input.use_video:
            self['demo'] = tuple_input.video_path
        elif tuple_input.use_camera:
            self['demo'] = 'camera'
        if tuple_input.save:
            # FIXME: We actually want to specify where to save the video to, currently not supported
            self['saveVideo'] = True

    def _parse_train_inputs(self, tuple_input: UserTrainInput):
        self['train'] = True  # Train it
        if tuple_input.use_gpu:
            self['gpu'] = 1.0
        self['lr'] = tuple_input.learning_rate
        self['batch'] = tuple_input.batch
        self['epoch'] = tuple_input.epoch
        self['save'] = tuple_input.save


def _get_dir(dirs):
    for d in dirs:
        this = os.path.abspath(os.path.join(os.path.curdir, d))
        if not os.path.exists(this): os.makedirs(this)


def easy_yolo(user_input):
    """
    yolo wrapper, facade
    """

    instructions = YoloArgs(user_input)

    requiredDirectories = [instructions.imgdir, instructions.binary, instructions.backup,
                           os.path.join(instructions.imgdir, 'out')]
    if instructions.summary:
        requiredDirectories.append(instructions.summary)

    _get_dir(requiredDirectories)

    # fix FLAGS.load to appropriate type
    try:
        instructions.load = int(instructions.load)
    except:
        pass

    tfnet = TFNet(instructions)

    if instructions.demo:
        tfnet.camera()
        exit('Demo stopped, exit.')

    if tfnet.train:
        print('Enter training ...')
        tfnet.train()
        if not instructions.savepb:
            exit('Training finished, exit.')

    if instructions.savepb:
        print('Rebuild a constant version ...')
        tfnet.savepb()
        exit('Done')

    tfnet.predict()
