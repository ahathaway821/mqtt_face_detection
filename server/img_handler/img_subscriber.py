import paho.mqtt.client as mqtt
import uuid
import os

LOCAL_MQTT_HOST = "broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

bucket_name = "w251-hw3-object-storage-bucket"

# First mount s3 bucket so we can write the file to the cloud
mount_result = os.system('./mount_s3.sh')

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")
        face_id = str(uuid.uuid4())
        
        # Write message payload to mounted s3 bucket
        with open("mount/" + face_id + ".png", "wb") as f:
            f.write(msg.payload)

    except Exception as e:
        print("Unexpected error:", e)


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
