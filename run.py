# Author: Nasrudin Bin Salim
# Copyright (C) Nasrudin B Salim 2018


# Arg parser Facade API pattern
# Receives arguments and then runs the YOLO program as required.

import argparse
from config import USE_GPU, SAVE_RESULTS, DEFAULT_VIDEO_SAVE_ADDRESS


def parse_args():
    parser = argparse.ArgumentParser(description='Run YOLOV2 Made Easy!')
    # Supply Video File
    parser.add_argument("video_path", help="Optional: Path to Video file", type=str)
    # Whether to use GPU
    parser.add_argument("-g", "--gpu", help="Whether to use GPU", action='store_true')
    # Where to save
    parser.add_argument("-s", "--save", help="Whether to save and where", action='store_true', type=str)

    args = parser.parse_args()

    video_path = args.video_path if args.video_path else False

    # Defaults
    save_directory = DEFAULT_VIDEO_SAVE_ADDRESS
    use_gpu = USE_GPU
    save_directory_bool = SAVE_RESULTS

    if args.gpu:
        use_gpu = True
        print("Using GPU")

    if args.save:
        print("Saving Result Video File")
        save_directory_bool = True

    if save_directory_bool and args.save is str:
        save_directory = args.save

    argument_dict = {"use_gpu": use_gpu,
                     "use_video": True if video_path else False,
                     "video_path": video_path if video_path else None,
                     "save": True if save_directory_bool else False,
                     "save_video_fp": save_directory if save_directory_bool else None}

    return argument_dict


if __name__ == '__main__':
    argument = parse_args()
    print(argument)
