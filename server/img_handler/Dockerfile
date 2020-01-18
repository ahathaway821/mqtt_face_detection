FROM ubuntu:18.04

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip

RUN apt install -y python-pip mosquitto-clients vim-tiny

RUN pip install paho-mqtt s3fs

ADD img_subscriber.py /

CMD ["python", "./img_subscriber.py"]