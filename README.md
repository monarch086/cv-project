# Image Processing and Computer Vision - Mini project

## Description

## Build

````sh
docker build -t detection-server -f ./Dockerfile .
docker-compose up -d

# To stop container:
docker-compose down
````

## Run

````sh
curl -X POST -F "image=path\to\image.jpg" http://192.168.0.55:5000/detect

curl -X POST -F "image=C:\Users\sbars\Downloads\bus.jpg" http://192.168.0.55:5000/detect
````
