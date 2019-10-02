FROM ubuntu:18.04
LABEL maintainer="Chris Schnaufer <schnaufer@email.arizona.edu>"

RUN apt update && \
    apt install -y python3