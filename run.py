# Author: Nasrudin Bin Salim
# Copyright (C) Nasrudin B Salim 2018


# Arg parser Facade API pattern
# Receives arguments and then runs the YOLO program as required.

import argparse

parser = argparse.ArgumentParser(description='Run YOLOV2 Made Easy!')

# Supply Video File
parser.add_argument("video_path", help="Optional: Path to Video file", type=str)

# Whether to use GPU
parser.add_argument("-g","--gpu", help="Whether to use GPU")

parser.add_argument("-s")
