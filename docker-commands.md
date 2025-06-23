# Docker Commands

- `docker`  
  Provides general information and options available for Docker commands.

- `docker -v`  
  Displays the version of Docker installed on your system.

- `docker run -it ubuntu`  
  Runs the Ubuntu image in interactive mode, allowing users to interact with the terminal inside the container.

- `docker container ls`  
  Lists all currently running containers.

- `docker container ls -a`  
  Lists all Docker containers, both running and stopped.

- `docker start <container_name>`  
  Starts a previously stopped container by specifying its name or ID.

- `docker stop <container_name>`  
  Stops a running container by specifying its name or ID.

- `docker exec -it <Container_name> bash`  
  Terminal will run interactively on your specific container <Container_name>.

- `docker images`  
  Gives information of all images available.
  
- `docker run -it <Image_name>`  
  Takes an image from Docker.com .
  
- `docker run -it mailhog/mailhog`  
  Fetching a mailhog(email) that can run inside the container.
  
- `docker run -it -p 1025:1025 mailhog`  
  > **-p** refers to port-mapping.  
  > first **1025** refers to our existing system port.  
  > **:** used to join the map from the map.  
  > second **1025** refers to the image's port.  
  > **mailhog** referes to the email.  

