import cv2
import time
import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST = "broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
print('Camera connected to local broker')

# 1 should correspond to /dev/video1
# your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

while(True):
    time.sleep(1)
    if not cap.isOpened():
        print('Unable to load camera')
        pass

    # Capture frame-by-frame
    ret, frame = cap.read()

    # We don't use the color information, so might as well save space
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # face detection
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:

        # cut out face from the frame..
        face = gray[y:y+h, x:x+w]
        rc, png = cv2.imencode('.png', face)
        msg = png.tobytes()

        local_mqttclient.publish(
            LOCAL_MQTT_TOPIC, payload=msg, qos=0, retain=False)


cap.release()
cv2.destroyAllWindows()
