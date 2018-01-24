
## Real-Time Video Recognition AI with auto-webscraping trainer + alerts
### By: Nasrudin Salim

#### Real-time object detection and classification with Yolo9000/Yolov2 algorithm
[Paper 1](https://arxiv.org/pdf/1506.02640.pdf) , [Paper 2](https://arxiv.org/pdf/1612.08242.pdf)  [darkflow](https://github.com/thtrieu/darkflow)   [darknet](http://pjreddie.com/darknet/yolo/) 

#### Test:
![ ](nas-demo.gif  "Algorithm Real-Time Demo")

### What is this:

- Automatically trains a class via webscraping image search results on a video recognition classifier with transfer learning.
- Enter a label, then enter a list of search queries to google for. It will then google for those search terms and fine-tunes a pretrained classifier.
- Detect objects as well as output alerts if an object in your "alert list" is found.
- Can be performed on a video stream in real-time.
- Can be performed on a live-camera stream in real-time.


### Prerequisities
1.  Python 3
2.  ffmpeg
3. OpenCV
4. OpenCV-Python
5. Tensorflow-GPU
6. CUDNN and CUDA ToolKit


# Usage
#### Getting Data
On the webscraper, indicate the label, as well as the search terms to use by editing it and change the parameters in downloadimages.py
In batch, type

	python downloadimages.py

#### Training
Once images are downloaded. You can download pretrained weights here: 
[darknet](https://pjreddie.com/darknet/yolo/) 
Or you can continue training your weights if you've done this before
Edit the parameters in train.py and then in batch type:

	python train.py

#### Testing/Using
You can test on either a video file, through video_run.py
You can test on a live webcam beed through camera_run.py

	python video_run.py
	python camera_run.py
	
You will be asked for the path of the video file. You can adjust the parameters as well as the paths of the weights by opening up the py files.

#### Testing/Using
You can test on either a video file, through video_run.py
You can test on a live webcam beed through camera_run.py

	python video_run.py
	python camera_run.py
	
You will be asked for the path of the video file. You can adjust the parameters as well as the paths of the weights by opening up the py files.

#### Setting Alerts
You can set alerts by editing the text file "alerts.txt" when a label found in this text file appears, it will generate an alert by drawing the box red and displaying "Alert x found in footage" when testing.




