FROM mcr.microsoft.com/vscode/devcontainers/python:1-3.11-bullseye

# Docker script args, location, and expected SHA - SHA generated on release
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG DOCKER_SCRIPT_SOURCE="https://raw.githubusercontent.com/microsoft/vscode-dev-containers/master/script-library/docker-debian.sh"
ARG DOCKER_SCRIPT_SHA="dev-mode"
ARG ENABLE_NONROOT_DOCKER="true"
ARG SOURCE_SOCKET=/var/run/docker-host.sock
ARG TARGET_SOCKET=/var/run/docker.sock


RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    # Verify common dependencies and utilities are installed
    && apt-get -y install --no-install-recommends apt-utils dialog git openssh-client curl less iproute2 procps 2>&1 \
    #
    # Create a non-root user to use if not already available - see https://aka.ms/vscode-remote/containers/non-root-user.
    && if [ $(getent passwd $USERNAME) ]; then \
    # If exists, see if we need to tweak the GID/UID
    if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then \
    groupmod --gid $USER_GID $USERNAME \
    && usermod --uid $USER_UID --gid $USER_GID $USERNAME \
    && chown -R $USER_UID:$USER_GID /home/$USERNAME; \
    fi; \
    else \
    # Otherwise ccreate the non-root user
    groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support for the non-root user
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME; \
    fi \
    #
    # Use Docker script from vscode script library to set things up
    && curl -sSL $DOCKER_SCRIPT_SOURCE -o /tmp/docker-setup.sh \
    && ([ "${DOCKER_SCRIPT_SHA}" = "dev-mode" ] || (echo "${DOCKER_SCRIPT_SHA} */tmp/docker-setup.sh" | sha256sum -c -)) \
    && /bin/bash /tmp/docker-setup.sh "${ENABLE_NONROOT_DOCKER}" "${SOURCE_SOCKET}" "${TARGET_SOCKET}" "${USERNAME}" \
    && rm /tmp/docker-setup.sh

# Install NVM, NPM and Node
RUN curl -sSL -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash \
    && bash -c 'source $NVM_DIR/nvm.sh \
    && nvm install --lts \
    && npm install -g prettier@2.0.5'

ENV PIPX_INSTAL="${PIPX_BIN_DIR}/pipx install --system-site-packages --pip-args=--no-cache-dir --pip-args=--force-reinstall"

# Setup additional python tools in a venv via pipx to avoid conflicts
RUN ${PIPX_INSTAL} poetry \
    && ${PIPX_INSTAL} pip-tools \
    && ${PIPX_INSTAL} pre-commit \
    && chown -R ${USER_UID}:${USER_GID} ${PIPX_HOME}

RUN apt-get install --no-install-recommends -y supervisor

RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d/

ENTRYPOINT [ "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]