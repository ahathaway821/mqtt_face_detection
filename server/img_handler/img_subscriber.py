import paho.mqtt.client as mqtt
import s3fs
import uuid

LOCAL_MQTT_HOST = "broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

bucket_name = "w251-hw3-object-storage-bucket"
fs = s3fs.S3FileSystem(anon=False)


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")

        face_id = str(uuid.uuid4())
        with fs.open(bucket_name} + "/" + face_id + ".png", 'wb') as f:
            f.write(msg)

    except Exception as e:
        print("Unexpected error:", e)


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
