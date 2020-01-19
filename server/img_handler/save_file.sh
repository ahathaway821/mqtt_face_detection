/bin/sh

ID=$1

s3fs w251-hw3-object-storage-bucket / -o nonempty -o url=https://s3.us-south.cloud-object-storage.appdomain.cloud -o passwd_file=$HOME/.passwd-s3fs
