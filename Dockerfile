# syntax=docker/dockerfile:1.4
FROM python:3.10-slim

WORKDIR /usr/server

COPY ./src /usr/server

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]