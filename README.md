# This repo contains shell scripts to automate installation of KubeEdge Cloud core (any Cloud) and Edge core (Raspberry Pi 4b)

#### "cloud-core-install.sh" contains scripts to install KubeEdge Cloud core
#### "obtain-token.sh" contains scripts to obtain the token required to join edge core to the KubeEdge cluster
#### "edge-core-install.sh" contains scripts to install edge core
#### "cloud-app-install.sh" contains scripts to install example application on the Cloud core
#### "edge-core-join.sh" to join the RPi edge node into the K8s cluster

# Order of running:

## On RPi edge core node:

 1) Prepare Raspberry Pi with Ubuntu server 20.04.2
 2) Setup networking on RPi and port forwarding if it is in Home network (port 22 needs to be forwarded for SSH and SCP)
 3) Check for public IP of the node
 4) enable root login on the node
    $ sudo su
    $ nano /etc/etc/ssh/sshd_config
    Change “PermitRootLogin without-password” to “PermitRootLogin yes”
    $ systemctl restart sshd
 5) change root password
    $ sudo su 
    $ passwd


## On Cloud core node:

 $ sudo su
 
 $ cd /root
 
 $ git clone https://github.com/wangso/KubeEdge-rpi-dev.git
 
 $ bash KubeEdge-rpi-dev/cloud-core-install.sh cloud_core_IP
 
 $ bash KubeEdge-rpi-dev/obtain-token.sh


## on Edge core node:

 $ sudo su
 
 $ cd /root
 
 $ git clone https://github.com/wangso/KubeEdge-rpi-dev.git
 
 $ bash KubeEdge-rpi-dev/edge-core-install.sh 
 
 $ bash KubeEdge-rpi-dev/edge-core-join.sh cloud_core_IP

## On Cloud core node:
 $ bash KubeEdge-rpi-dev/cloud-app-install.sh

