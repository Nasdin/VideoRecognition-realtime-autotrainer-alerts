
## Real-Time Video Recognition AI with auto-webscraping trainer + alerts
### By: Nasrudin Salim

#### Real-time object detection and classification with Yolo9000/Yolov2 algorithm
[Paper 1](https://arxiv.org/pdf/1506.02640.pdf) , [Paper 2](https://arxiv.org/pdf/1612.08242.pdf)  [darkflow](https://github.com/thtrieu/darkflow)   [darknet](http://pjreddie.com/darknet/yolo/) 

#### Test:
![ ](nas-demo.gif  "Algorithm Real-Time Demo")

### What is this:

- Automatically trains a model via webscraping image search results on a video recognition classifier with transfer learning.
- Enter a label, then enter a list of search queries to google for. It will then google for those search terms and fine-tunes a pretrained classifier.
- Detect objects as well as output alerts/colors differently if an object in your "alert list" is found.
- Can be performed on a video stream in real-time.
- Can be performed on a live-camera stream in real-time.


### Prerequisities
0. Anaconda 3
1.  Python 3
2. CUDNN and CUDA ToolKit Installed
3. GPU with CUDA 9.0 and above support

## Installation Instructions:
- A conda environment file has been provided, please make use of environment file to install the necessary requirement packages.


		conda create -n "YourEnvironmentName" -f environment.yml

Remember to download pretrained weights if you need to
See training section

# Usage
#### Getting Data
On the webscraper, indicate the labels in labels.txt, as well as the search terms to use by editing it and change the parameters in config.py then in terminal, type


		python downloadimages.py

#### Training
Once images are downloaded. You can download pretrained weights here: 
[darknet](https://pjreddie.com/darknet/yolo/) 
Or you can continue training your weights if you've done this before
Edit the parameters in train.py and then in batch type:

		python train.py -g


	-g : Whether to use GPU
	-e #: Epochs (optional)
	-s #: Save Rate (optional)
	-e #: Epochs (optional)
	-lr #: Learning Rate (optional)
	-b #: Batch (optional)


#### Testing/Using
Usage:

	python run.py "path_to_video_file" -g -s "test.avi"
	
#### Explanation

	Whether to use a video file, supply path
	If not video file, assume to use camera feed.
	-g /--gpu : Optional, whether to use GPU ( Defaults to config)
	-s /--save: Optional, whether to save results to a video file and where (Defaults to config)

### Configs

There is a config.py provided which helps to set the defaults for the following:
1. 	Edit the path to weight file
2. 	USE GPU? Bool
3. 	SAVE Result video file? Bool


You will be asked for the path of the video file. You can adjust the parameters as well as the paths of the weights by opening up the py files.

#### Setting Alerts
You can set alerts by editing the text file "alerts.txt" when a label found in this text file appears, it will generate an alert by drawing the box red and displaying "Alert x found in footage" when testing.

#### HELP AND CONTRIBUTION

	This project needs your help and contribution
	The Training Script needs work.
	The Alerts and Pinging requires work to finish.
	Downloading of images from google and seamless Training


