# Author: Nasrudin Bin Salim
# Copyright (C) Nasrudin B Salim 2018


# Arg parser Facade API pattern
# Receives arguments and then runs the YOLO program as required.

import argparse
from config import USE_GPU, SAVE_RESULTS, DEFAULT_VIDEO_SAVE_ADDRESS


def parse_args():
    parser = argparse.ArgumentParser(description='Run YOLOV2 Made Easy!')
    # Supply Video File
    parser.add_argument("video_path", help="Optional: Path to Video file", action='store', default="", nargs='?')
    # Whether to use GPU
    parser.add_argument("-g", "--gpu", help="Whether to use GPU", action='store_true')
    # Where to save
    parser.add_argument("-s", "--save", help="Whether to save and where", action='store', default=False,
                        nargs='?')

    args = parser.parse_args()

    # Defaults
    save_directory = DEFAULT_VIDEO_SAVE_ADDRESS
    use_gpu = USE_GPU
    save_directory_bool = SAVE_RESULTS
    use_camera = True
    use_video = False
    video_path = ""

    if args.video_path is not "":
        use_camera = False
        video_path = args.video_path
        if not video_path.lower().endswith("avi"):
            print("Not a .avi file")
        use_video = True
        print("Using Video file {} to load into YOlO".format(video_path))
    else:
        print("Using Camera")

    if args.gpu:
        use_gpu = True
    if use_gpu:
        print("Using GPU")
    if args.save or args.save is None:
        save_directory_bool = True
    if save_directory_bool:
        if isinstance(args.save, str):
            save_directory = args.save
        print("Saving Result Video File to {}".format(save_directory))

    argument_dict = {"use_gpu": use_gpu,
                     "use_video": use_video,
                     "use_camera": use_camera,
                     "video_path": video_path,
                     "save": True if save_directory_bool else False,
                     "save_video_fp": save_directory if save_directory_bool else None}

    return argument_dict


if __name__ == '__main__':
    argument = parse_args()
    print(argument)
