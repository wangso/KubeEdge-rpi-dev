# This repo contains shell scripts to automate installation of KubeEdge Cloud core (any Cloud) and Edge core (Raspberry Pi 4b)

#### "cloud-core-install.sh" contains scripts to install KubeEdge Cloud core
#### "obtain-token.sh" contains scripts to obtain the token required to join edge core to the KubeEdge cluster
#### "edge-core-install.sh" contains scripts to install edge core
#### "cloud-app-install.sh" contains scripts to install example application on the Cloud core
#### "edge-core-join.sh" to join the RPi edge node into the K8s cluster

## Order of running:
#### 1) Prepare Raspberry Pi with Ubuntu server 20.04.2
#### 2) Setup networking on RPi and port forwarding if it is in Home network (port 22 needs to be forwarded for SSH and SCP)
#### 3) Run "cloud-core-install.sh"  on the Cloud node
#### 4) Run "obtain-token.sh"  on the Cloud node
#### 5) Run "edge-core-install.sh"  on the RPi
#### 6) Run "cloud-app-install.sh"  on Cloud node
#### 7) Run "edge-core-join.sh" on RPi

## Make sure you follow the notes in the scripts

