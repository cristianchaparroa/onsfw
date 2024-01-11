FROM tensorflow/tensorflow:latest-gpu
WORKDIR /

ENV DEBIAN_FRONTEND noninteractive
COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN python3 -m pip cache purge 
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir --no-warn-script-location -r requirements.txt 

CMD ["python3", "main.py"]
