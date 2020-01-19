import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST = "broker"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

REMOTE_MQTT_HOST = "52.116.7.151"
REMOTE_MQTT_PORT = 1883
REMOTE_MQTT_TOPIC = "faces"


def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        print("message received!")
        remote_mqttclient.publish(REMOTE_MQTT_TOPIC,
                                  payload=msg.payload,
                                  qos=0,
                                  retain=False)
    except Exception as e:
        print("Unexpected error:", e)


# Instantiate and connect to local broker with local mqtt client
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# Instantiate and connect to remote mqtt broker
remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_local
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)

# go into a loop
local_mqttclient.loop_forever()
