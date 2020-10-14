# Kubernetes Stafford
[![GitHub](https://img.shields.io/github/license/jacobmannix/kubernetes-stafford?color=blue)](LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/jacobmannix/kubernetes-stafford)
[![GitHub last commit](https://img.shields.io/github/last-commit/jacobmannix/kubernetes-stafford)](/commits/master)

> <b> This project is a based off my project [stafford-racing-twitter-bot](https://github.com/JacobMannix/stafford-racing-twitter-bot) built into a docker container and orchestrated by kubernetes. Kubernetes files include a cronjob for scheduling the script, a secret for securely storing api keys and a persistent volume and associated claim for storing the updated title used by the script. </b>

#
### Docker Image
The docker image can be found at [dockerhub/stafford-app](https://hub.docker.com/repository/docker/jmannix3/stafford-app). All the specifics of the contents of the image and python app can be found at the [stafford-racing-twitter-bot](https://github.com/JacobMannix/stafford-racing-twitter-bot) repo.

#
### Kubernetes
The necessary files to run this project with kubernetes are contained within the [kubernetes](/kubernetes) folder.
- [stafford-secrets-example.yaml](/kubernetes/secrets) - used to mount a volume with the necessary secrets accessable to the pod containing the docker container for the app
- [stafford-pv.yaml](/kubernetes/services) - create a necessary persistent volume
- [stafford-pvc.yaml](/kubernetes/services) - create the necessary persistent volume claim needed to store the file in the [data](/src/data) folder.
- [stafford-cj.yaml](/kubernetes/services) - contains the necessary information to access the secrets volume and persistant volume needed by the app

#
Licensed under the [MIT License](LICENSE).
