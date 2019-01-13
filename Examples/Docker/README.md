##Using ModemStatus in a docker container

Example: Gather statistics every 5 minutes, updating graphs every 25. Serving the graphs from another docker container
```
git clone https://github.com/codytrey/ModemStatus.git
cd ModemStatus/Examples/Docker
mkdir modemstatus
docker build .
docker run -d --mount type=bind,source="$(pwd)"/modemstatus,target=/tmp/modemstatus ${IMAGEID}
sudo docker run -d -v $(pwd)/modemstatus:/content -e FOLDER=/content -p 8080:8080 halverneus/static-file-server:latest
```