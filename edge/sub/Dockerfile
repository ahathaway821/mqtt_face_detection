FROM alpine:3.7

RUN apk add mosquitto
RUN apk add mosquitto-clients
RUN apk add py-pip
RUN pip install paho-mqtt

ADD face_subscriber.py /

CMD ["python", "./face_subscriber.py"]