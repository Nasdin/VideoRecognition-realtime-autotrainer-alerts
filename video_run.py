# Author: Nasrudin Bin Salim
# Copyright (C) Nasrudin B Salim 2018
from util.parser import yolo_run
from config import *

# Parameters here

## Path to model and weight
model_cfg = MODEL_CFG_FILE_PATH
model_weight = MODEL_WEIGHT

# Bools
use_gpu = USE_GPU
save_results = SAVE_RESULTS


def main():
    video_file = input("Path to video file: ")
    yolo_run(model=model_cfg,weights=model_weight,video_file_or_camera=video_file,use_gpu=use_gpu,save_results=save_results)



if __name__ == '__main__':
    main()





