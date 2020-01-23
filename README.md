# MQTT Face Detection

This is a an app to experiment primarily with MQTT and OpenCV while passing messages between an edge device and the cloud.

Using a USB webcam on an edge device (NVIDIA Jetson TX2), the goal is to capture human faces, publish the face to a edge MQTT broker, and then have that broker publish the message to a server broker hosted in the cloud.

Once the server broker receives the message, it stores the face image in S3.

For both the local broker and the cloud broker, I used the same topic name, faces, as the image detection capabilities could hypothetically publish different types of images and we might want to group them with different topics.
