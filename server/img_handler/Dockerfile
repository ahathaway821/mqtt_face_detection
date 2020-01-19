FROM ubuntu:18.04

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip

RUN apt install -y python-pip mosquitto-clients vim-tiny

RUN apt-get install -y automake autotools-dev g++ git libcurl4-gnutls-dev
RUN apt-get install -y libfuse-dev libssl-dev libxml2-dev make pkg-config fuse

RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y mime-support

RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git

WORKDIR s3fs-fuse/

RUN ./autogen.sh
RUN ./configure

RUN make
RUN make install
RUN s3fs --version

RUN pip install paho-mqtt
ADD img_subscriber.py /s3fs-fuse
ADD save_file.sh /s3fs-fuse

RUN chmod +x save_file.sh

ENV ACCESSKEYID=ecad1ec6923f4ddbb9f12d43e19ee82d
ENV SECRETACCESSKEY=e91acfd5010616257d8c62f6993ea66bf6bd2764086d92ca

RUN echo $ACCESSKEYID:$SECRETACCESSKEY > /$HOME/.passwd-s3fs
RUN chmod 600 /$HOME/.passwd-s3fs

CMD ["python", "-u", "./img_subscriber.py"]
