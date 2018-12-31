# ecsdemo
This is a simple webserver. It listens on default port 8080 on all interfaces.

# Environment variables
* PORT=wxyz (Port to listen on. Default port is 8080)
* VER="user given string" (This string is added to every http response)

# Requirements
* Python 3.7.1
* requests

# Docker run command
```
# Runs the container with external port 80 mapped to internal port 8080
docker run -d -p 80:8080 aniapte/ecsdemo:latest
```

# Sample http response
```
root@ip-10-21-11-11:~# curl localhost
load_cpu: False

VER: VER not set
pid: 1
instance_id: i-xxxxxxxxxxxxx
container_id: /docker/51830fc56d030ba486ca8129f8d97c02f8ae4619104246afc7dc4b8854a0be53

```