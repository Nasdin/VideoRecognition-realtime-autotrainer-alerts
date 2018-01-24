# Author: Nasrudin Bin Salim
# Copyright (C) Nasrudin B Salim 2018
from util.parser import yolo_run


# Parameters here

## Path to model and weight
model_cfg = 'weights/yolo-voc.cfg'
model_weight = 'weights/yolov2.weights'

# Bools
use_gpu = True
save_results = True


def main():
    video_file = input("Path to video file: ")
    yolo_run(model=model_cfg,weights=model_weight,video_file_or_camera=video_file,use_gpu=use_gpu,save_results=save_results)



if __name__ == '__main__':
    main()





