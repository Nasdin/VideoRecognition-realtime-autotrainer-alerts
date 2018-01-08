
## Detecting burning cars in real-time video feeds by Nasrudin Salim
## This project is still a WIP

Real-time object detection and classification. Paper: [version 1](https://arxiv.org/pdf/1506.02640.pdf) , [Version 2](https://arxiv.org/pdf/1612.08242.pdf) 

### The Yolo algorithm
The YOLO algorithm was forked from [darkflow](https://github.com/thtrieu/darkflow) which was taken from darknet. Read more about Darknet and Yolo [here](http://pjreddie.com/darknet/yolo/) 

### My work:
Using the research and work done discussed in the papers above, create and classify a model which detects burning cars in **real-time** from video streams.

### Materials and Data, feature engineering
I used a webscraper and google image search to scrape for pictures and gifs of burning cars using python scripts. Followed by manipulating the images downloaded to create a more robust trained model.

### Tests
Using a webcam, point webcam to videos of burning cars, either from movies or from youtube clips. It should classify burning cars when one is present.

### Results

### Further work
When a burning car is detected, we can move onto another pipeline towards output and send an alert.
