# Stafford-app docker container and kuberentes files

![GitHub](https://img.shields.io/github/license/jacobmannix/kubernetes-stafford?color=blue)

#
> This is a python script built into a docker container and orchestrated by kubernetes. Kubernetes files include a cronjob for scheudled the script, a secret for securely storing api keys and a persistent volume and associated claim for storing the updated title used by the script.

includes a few libraries, to add or remove libraries see [requirements.txt](.devcontainer/requirements.txt)
- [Github](https://github.com/JacobMannix/docker_python)
- [Docker Hub Image](https://hub.docker.com/repository/docker/jmannix3/docker_python)

#
### Apps used
- [Docker](https://www.docker.com/) - Dockerfile, docker-compose.yaml
- [Visual Studio Code](https://code.visualstudio.com/) - .vscode
- Python - .py
- Kubernetes - yaml(s) in kubernetes folder

#
Licensed under the [MIT License](LICENSE).
