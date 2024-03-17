# Image Processing and Computer Vision - Mini project

## Description

Project for detecting objects on images based on YOLOv8 model. It consists of the server, which takes images with requests, detects objects and sends list of found objects in the response.

YOLO (You Only Look Once) is a popular open source neural network model for object detection developed by [Ultralytics](https://docs.ultralytics.com/) team.

## Build

````sh
# To build image:
docker build -t detection-server -f ./Dockerfile .

# To start container:
docker-compose up -d

# To stop container:
docker-compose down
````

## Run

````sh
curl -X POST -F "image=path\to\image.jpg" http://192.168.0.55:5000/detect

curl -X POST -F "image=C:\Users\sbars\Downloads\bus.jpg" http://localhost/detect
````

Response format:

````json
{
    "image":"bus.jpg",
    "objects":"[\"bus: 0.970683753490448\"]",
    "timestamp":"2024-03-17T16:35:03.214512"
}
````
