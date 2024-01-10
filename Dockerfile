FROM tensorflow/tensorflow:2.14.0-gpu
WORKDIR /

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN python3 -m pip install --upgrade opennsfw2 tensorrt 

COPY . .

RUN python3 test.py
