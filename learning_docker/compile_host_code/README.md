# Bind Mounts

After building yout Docker image, you can run the container with some setup bind-
mounts. This methos allows you to modify source code in your host machine and
build it inside the container where the environment is nicely setup for it. You
can bind-mount as many directories and files as you need as specified in the docker-
compose file. Moroever, you can specify if you want the bind-mounts to be read-only.
In this case, you can only make modifications from the host machine into the
container.

# Build inside Docker Container

  * Install [Docker-Compose](https://docs.docker.com/compose/install/#prerequisites)
  if you have not done so already:

		$ sudo curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

  * Build Docker image:

		$ cd path/to/compile_host_code
		$ docker build -t temporary_image -f dockerfiles/dockerfile .

  * Run the container with docker-compose to bind-mount some source directories:

		$ cd path/to/compile_host_code/dockerfiles
		$ docker-compose up -d
		$ docker attach [container name]

**NOTES**:
  * If nothing shows up on screen after the last command, press ENTER to
	access the terminal.
