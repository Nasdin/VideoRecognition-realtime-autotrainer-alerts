from util.parser.defaults import argHandler

from collections import namedtuple

UserRunInput = namedtuple("UserRunInputs",
                          ['use_gpu', 'use_video', 'use_camera', 'video_path', 'save', 'save_video_fp'])
UserTrainInput = namedtuple("UserTrainInputs", ['use_gpu', 'epoch', 'save', 'learning_rate', 'batch'])

from config import MODEL_CFG_FILE_PATH, MODEL_WEIGHT


class YoloArgs(argHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Need to set the model and weight paths
        self['model'] = MODEL_CFG_FILE_PATH
        self['load'] = MODEL_WEIGHT

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
            # FIXME: We actually want to specify where to save the video to
            self['saveVideo'] = True

    def _parse_train_inputs(self, tuple_input: UserTrainInput):
        if tuple_input.use_gpu:
            self['gpu'] = 1.0
        self['lr'] = tuple_input.learning_rate
        self['batch'] = tuple_input.batch
        self['epoch'] = tuple_input.epoch
        self['save'] = tuple_input.save


# execute clihandler via python
def _execute_yolo(commandstring):
    command = [""] + commandstring.split(" ")
    print("executing command", command)
    cliHandler(command)
