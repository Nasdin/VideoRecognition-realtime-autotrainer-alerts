
## Detecting burning cars in real-time video feeds by Nasrudin Salim
Automated data downloading through an automated webscraper routine, data munging and automated transfer learning and reclassification of a pretrained yolo algorithm
## This project is still a WIP

Real-time object detection and classification. Paper: [version 1](https://arxiv.org/pdf/1506.02640.pdf) , [Version 2](https://arxiv.org/pdf/1612.08242.pdf) 

### The Yolo algorithm
The YOLOV2 algorithm was forked from [darkflow](https://github.com/thtrieu/darkflow) which was taken from darknet. Read more about Darknet and Yolo [here](http://pjreddie.com/darknet/yolo/) 

### My work:
Using the research and work done discussed in the papers above, create and classify a model which detects burning cars in **real-time** from video streams.

### Materials and Data, feature engineering
I used a webscraper and google image search to scrape for pictures and gifs of burning cars using python scripts. Followed by manipulating the images downloaded to create a more robust trained model.

### Tests
- Using a webcam, point webcam to videos of burning cars, either from movies or from youtube clips. It should classify burning cars when one is present.
- Use a video file, run the algorithm on the video file and watch it classify in real time

# Usage
#### Getting Data
Download data from the internet using the webscraper
In batch, type

	python downloadimages.py
		

# Process Flow / How it Works	
1. Pictures of a specific search are downloaded from an automated google search and webscraping e.g Burning cars
2. The pictures are verified with VGG16 model to contain a specific image e.g Car
3. The pictures are then split to train and test proportions in the train test sub folders
4. A yolov2 model is created with pretrained weights
5. The yolov2 model is retrained with transfer learning to classify the new category
6. The newly trained yolov2 model is saved and ready for usage

## Results
This is still a WIP

### Further work
When a burning car is detected, we can move onto another pipeline towards output and send an alert.



