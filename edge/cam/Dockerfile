FROM ubuntu:18.04

ARG URL=http://169.44.201.108:7002/jetpacks/4.3

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip
RUN apt install -y curl

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

RUN curl $URL/libopencv_3.3.1-2-g31ccdfe11_arm64.deb  -so libopencv_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-dev_3.3.1-2-g31ccdfe11_arm64.deb
RUN curl $URL/libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb -so libopencv-python_3.3.1-2-g31ccdfe11_arm64.deb

RUN apt remove -y libopencv-calib3d-dev libopencv-core-dev 

RUN apt install -y  libtbb-dev libavcodec-dev libavformat-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk2.0-dev
RUN apt install -y libswscale-dev libv4l-dev
RUN dpkg -i *.deb

RUN apt install -y libcanberra-gtk-module libcanberra-gtk3-module libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev 

RUN apt install -y python-pip mosquitto-clients vim-tiny
RUN pip install paho-mqtt
RUN pip install numpy

WORKDIR /
ADD face_detection.py /
ADD haarcascade_frontalface_default.xml /

CMD ["python", "./face_detection.py"]