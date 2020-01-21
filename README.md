# MQTT Face Detection

This is a an app to experiment primarily with MQTT and OpenCV while passing messages between an edge device and the cloud.

Using a USB webcam on an edge device (NVIDIA Jetson TX2), the goal is to capture human faces, publish the face to a edge MQTT broker, and then have that broker publish the message to a server broker hosted in the cloud.

Within the edge folder, there is a docker-compose.yml file that spins up a mqtt broker, an ubuntu based face detection service that publishes images to the broker, and a subscriber that upon receiving a face from the broker, will publish the image to another broker hosted in the cloud.

Within the server folder, there is a docker-compose.yml file that spins up a mqtt broker and an ubuntu based subscriber that will save images received by the broker to s3 storage.

For all of the mqtt messaging, I went with service level 0 because a) I wanted to test the data loss, and b) because the face detection captures so many images, I wasn't particularly concerned if an image or two got lost in the ether.
