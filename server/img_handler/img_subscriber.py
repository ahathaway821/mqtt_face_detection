import paho.mqtt.client as mqtt
#import s3fs
import uuid
import os

LOCAL_MQTT_HOST = "broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

bucket_name = "w251-hw3-object-storage-bucket"
key="ecad1ec6923f4ddbb9f12d43e19ee82d"
secret="e91acfd5010616257d8c62f6993ea66bf6bd2764086d92ca"
#fs = s3fs.S3FileSystem(anon=False, key=key, secret=secret)

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")
        face_id = str(uuid.uuid4())
        #with fs.open(bucket_name + "/" + face_id + ".png", 'w') as f:
        #    f.write(msg.payload)
        os.system('./save_file.sh ' + face_id)

    except Exception as e:
        print("Unexpected error:", e)


local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
