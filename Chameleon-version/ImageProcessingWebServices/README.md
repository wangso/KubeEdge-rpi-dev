# ImageProcessingWebServices

## Object Detection

### Server 
[server.py](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/Server/server.py) implements a RESTFUL webservice for object detection.
The following endpoints currently exist.
1. /frameProcessing: This uses openCv methods to find the objects that have changed from a preceding frame. It sends each object to /classifier.
2. /objectClassifier: This is a deep learning model(Yolo-V3 trained on COCO) that attempts to classify an image into a fixed set of classes. It increments the [counter](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/output/server/output.txt) for that object class.
3. /init: This initializes all counters to 0
4. /getCounts: This retrieves the current value of the counters.

[Dockerfile](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/Server/Dockerfile) for starting up a container running the server.

[server-deployment.yaml](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/server-deployment.yaml) for starting up a k8s pod running the server.

### Client 
[client.py](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/Client/client.py) reads a video and sends frames to server.py.

[Dockerfile](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/Client/Dockerfile) for starting up a container running the client.

[client-deployment.yaml](https://github.com/wangso/KubeEdge-rpi-dev/blob/master/Chameleon-version/ImageProcessingWebServices/client-deployment.yaml) for starting up a k8s pod running the client.

### Testing with Docker containers only

1. Run server container : 

    $ docker pull wangso:imgproc-server:V1 
    
    $ docker run --name server -v /root/server:/ImageProcessingWebServices/output/server -p 5000:5000 wangso:imgproc-server:V1
    
2. Observe the logs from the server:
    
    $ docker logs -f server
    
3. On command line (replace Server_IP:Port):

    $ curl -X POST -H 'Content-Type: application/json' https://Server_IP:Port/setNextServer -d '{"server":"Server_IP:Port"}'
    
3. Run client container : 
    
    $ docker pull wangso:imgproc-client:V1 
    
    $ docker run --name client -v /root/client:/ImageProcessingWebServices/output/client --env server=Server_IP:Port wangso:imgproc-client:V1
    
### Testing with Kubernetes cluster
1. Run server deployment:

    $ kubectl apply -f server-deployment.yaml
    
2. Monitor server output:

    $ kubectl logs -f server_pod_ID

3. Update server address to listen to (URL is depending on if the host machine has TLS, change to HTTP if no TLS on the host)

    $ curl -X POST -H 'Content-Type: application/json' https://Server_IP:Port/setNextServer -d '{"server":"Server_IP:Port"}'
    
3. Run client deployment (first modify the env inside yaml file to update the server_IP:port): 

     $ kubectl apply -f client-deployment.yaml
