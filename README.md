# kubernetes stafford
![GitHub](https://img.shields.io/github/license/jacobmannix/kubernetes-stafford?color=blue)
![GitHub top language](https://img.shields.io/github/languages/top/jacobmannix/kubernetes-stafford)
![GitHub last commit](https://img.shields.io/github/last-commit/jacobmannix/kubernetes-stafford)
#
This project is a based off my project [stafford-racing-twitter-bot](https://github.com/JacobMannix/stafford-racing-twitter-bot) built into a docker container and orchestrated by kubernetes. Kubernetes files include a cronjob for scheudled the script, a secret for securely storing api keys and a persistent volume and associated claim for storing the updated title used by the script.
#
### Docker Image
The docker image can be found at [dockerhub/stafford-app](https://hub.docker.com/repository/docker/jmannix3/stafford-app). All the specifics of the contents of the image and python app can be found at the [stafford-racing-twitter-bot](https://github.com/JacobMannix/stafford-racing-twitter-bot) repo.
#
Licensed under the [MIT License](LICENSE).
