# kubeedge ai demo
## Description
This demo contains two general modules: AI algorithm module and a zigbee device module.
## Prerequisites  
### Hardware Prerequisites  
1. CC2531 USB sniffer with firmware been refreshed
<img src="./image/cc2531.jpg" width=256 height=256 />
2. Xiao Mi zigbee power plug ZNCZ02LM
<img src="./image/switch.jpg" width=256 height=256 />  
3. Raspberry pi 4b 
<img src="./image/raspberrypi.jpg" width=256 height=256 /> 

### Software Prerequisites  
1. KubeEdge (v1.4+)
## Steps to reproduce
1. Clone the project 
2. Run KubeEdge
### AI algorithm module
#### Face recognition    
``` 
    $ cd face-recong  
    $ docker build -t face-recon:dev  
    $ cd ..
    $ kubectl apply -f faceReconDeployment.yaml
 ```  
1. Calling the camera defaults to a local camera, and you can change the IP address of the camera by using `-- camera = ip:port`  
2. You can add the `--show` parameter to determine whether the recognition results are displayed on the display.  
3. When adding the `--show` parameter, you can pass in face data via the S key on the keyboard  
4. Copy the model to the local `/model/facenet` directory before running it
#### Moving object detection  
``` 
    $ cd motion detection  
    $ docker build -t motion-detection:dev 
    $ cd ..
    $ kubectl apply -f motionDetectionDeployment.yaml
 ```    
1. The camera information configuration is the same as face recognition
2. When a moving object appears in front of the camera, the program will record the video and save the result to the local directory /data/video
### Device module
#### Device & DeviceModel
``` 
    $ cd crds
    $ kubectl apply -f devicemodel.yaml
    $ kubectl apply -f device.yaml
 ```    
When the device is connected, you can view the results of the cloud device synchronization through the following command
``` 
    $ kubectl get device switch -oyaml -w 
```  
#### zigbee2mqtt  
``` 
    $ cd zigbee2mqtt
    $ docker build -t zigbee2mqtt:v1 .
    $ cd ..
    $ kubectl apply -f deployzigbee2mqtt.yaml
```
1. Make sure cc2531 USB Sniffer is connected to your device and there is a directory `/dev/ttyacm0`
#### mapper
``` 
    $ cd mapper
    $ docker build -t mapper:v1 .
    $ kubectl apply -f deployMapper.yaml  
```  
During face recognition, the ZigBee switch will be turned on if the recognition result exists in the face database. If the result is unknown, the Zigbee switch will be turned off. The status information of the switch can be viewed through the Device Switch in the cloud.
