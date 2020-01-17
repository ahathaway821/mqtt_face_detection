FROM ubuntu

RUN apt update

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install -y python-opencv python-pip mosquitto-clients libopencv-dev vim-tiny
RUN pip install paho-mqtt

ADD face_detection.py /
ADD haarcascade_frontalface_default.xml /

CMD ["python", "./face_detection.py"]