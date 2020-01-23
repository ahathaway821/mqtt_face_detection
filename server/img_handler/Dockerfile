FROM ubuntu:18.04

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip
RUN apt install -y python-pip mosquitto-clients vim-tiny
RUN apt-get install -y automake autotools-dev g++ git libcurl4-gnutls-dev
RUN apt-get install -y libfuse-dev libssl-dev libxml2-dev make pkg-config fuse
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y mime-support

RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git
RUN mkdir /s3fs-fuse/mount
WORKDIR s3fs-fuse/

RUN ./autogen.sh
RUN ./configure

RUN make
RUN make install
RUN s3fs --version

RUN pip install paho-mqtt
ADD img_subscriber.py /s3fs-fuse
ADD mount_s3.sh /s3fs-fuse

RUN chmod +x mount_s3.sh

ENV ACCESSKEYID=
ENV SECRETACCESSKEY=

RUN echo $ACCESSKEYID:$SECRETACCESSKEY > /$HOME/.passwd-s3fs
RUN chmod 600 /$HOME/.passwd-s3fs

CMD ["python", "-u", "./img_subscriber.py"]
