# Summary

Files in this directory are examples of different applications and services Docker
has to offer.

# Installation

1. Install [Docker](https://docs.docker.com/get-started/#setup):

		$ sudo apt-get install docker

2. Register username to docker group:

		$ sudo usermod -aG docker $(whoami)

3. Install [Docker-Compose](https://docs.docker.com/compose/install/#prerequisites):

		$ sudo curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

## Problem: Docker Container Can't Access Internet

Taken from: [SCRIMMAGE README](https://github.com/gtri/scrimmage/blob/master/README.md)

Docker can have DNS issues. If you can ping a public ip address within a docker
image (such as 8.8.8.8), but you can't ping archive.ubuntu.com, create the file
/etc/docker/daemon.json with the following contents:

    {
        "dns": ["<DNS-IP>", "8.8.8.8"]
    }

Where <DNS-IP> is the first DNS IP address and <interfacename> is a network
interface with internet access from the commands:

    $ nmcli dev list | grep 'IP4.DNS'                    # Ubuntu <= 14
    $ nmcli device show <interfacename> | grep IP4.DNS   # Ubuntu >= 15

Restart docker:

    $ sudo service docker restart

# Bind Mounts: compile_host_code

After building yout Docker image, you can run the container with some setup bind-
mounts. This methos allows you to modify source code in your host machine and
build it inside the container where the environment is nicely setup for it. You
can bind-mount as many directories and files as you need as specified in the docker-
compose file. Moroever, you can specify if you want the bind-mounts to be read-only.
In this case, you can only make modifications from the host machine into the
container.

1. Build Docker image:

		$ cd path/to/compile_host_code
		$ docker build -t temporary_image -f dockerfiles/dockerfile .

2. Run the container with docker-compose to bind-mount some source directories:

		$ cd path/to/compile_host_code/dockerfiles
		$ docker-compose up -d
		$ docker attach [container name]

	**NOTE**: If nothing shows up on screen after the last command, press ENTER to
	access the terminal.

# Run GUI App Inside Container: gui_inside_container

Out of the box, it is not allowed to run GUI apps inside a Docker container.
[This blog](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
explains how to build and run a Docker image such that you can run GUI apps inside
the container.

1. Build Docker image:

		$ cd path/to/gui_inside_container
		$ docker build -t temporary_image .

2. Run the container:

		$ docker rin -it --rm \
		-e DISPLAY=$DISPLAY \
		-v /tmp/.X11-unix:/tmp/.X11-unix \
		temporary_image
