FROM python:3.8-slim-buster

# Options for common setup script
# ARG INSTALL_ZSH="true"
# ARG UPGRADE_PACKAGES="false"
# ARG USERNAME=vscode
# ARG USER_UID=1000
# ARG USER_GID=$USER_UID

RUN mkdir -p /app
WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD ./src/ /app/
