# This repo contains shell scripts to automate installation of KubeEdge Cloud core (any Cloud) and Edge core (Raspberry Pi 4b)

#### "cloud-core-install.sh" contains scripts to install KubeEdge Cloud core
#### "obtain-token.sh" contains scripts to obtain the token required to join edge core to the KubeEdge cluster
#### "edge-core-install.sh" contains scripts to install edge core
#### "cloud-app-install.sh" contains scripts to install example application on the Cloud core
#### "edge-core-join.sh" to join the RPi edge node into the K8s cluster



# Working installation on GCP/AWS/GENI

## On edge core nodes:

1)	Switch to sudo 

      $ sudo su
   
      $ cd /root
    
      $ export PATH=$PATH:/snap/bin
     
2)	Setup Root SSH login with password (the string to replace might be different depending on your OS)

      $ sed -i "s/PermitRootLogin prohibit-password/PermitRootLogin yes/g" /etc/ssh/sshd_config 

      $ sed -i "s/PasswordAuthentication no/PasswordAuthentication yes/g" /etc/ssh/sshd_config
   
      $ systemctl restart sshd
   
3)	Setup root password

      $ passwd

      And add your own password 

## On cloud core node:

      $ sudo su
 
      $ cd /root
 
      $ git clone https://github.com/wangso/KubeEdge-rpi-dev.git
 
      $ bash /root/KubeEdge-rpi-dev/Chameleon-version/kubeedge-cloud-install/cloud-core-install.sh $cloud_core_IP
 
      $ bash /root/KubeEdge-rpi-dev/Chameleon-version/kubeedge-cloud-install/obtain-token.sh

## On each edge core node:

      $ sudo su
 
      $ cd /root
 
      $ git clone https://github.com/wangso/KubeEdge-rpi-dev.git
 
      $ bash /root/KubeEdge-rpi-dev/Chameleon-version/kubeedge-edge-install/edge-core-install.sh 
 
      $ bash /root/KubeEdge-rpi-dev/Chameleon-version/kubeedge-edge-install/edge-core-join.sh $cloud_core_IP $token $edge_node_name



