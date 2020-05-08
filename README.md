## Basic blog site.

This web application creates an very basic blog site using Django. The site allows blog authors to create text-only 
blogs using the Admin site, and any logged in user to add comments via a form. Any user can list all bloggers, all 
blogs, and detail for bloggers and blogs (including comments for each blog).

## [Docker](https://www.docker.com/) desription.

### Compose files
Docker compose files allow the specification of complex configurations of multiple inter-dependent
services to be run together as a cluster of docker containers. Consult the excellent docker-compose
[reference](https://docs.docker.com/compose/compose-file/) to learn about the many different
configurable settings. Compose files are written in [`.yaml`](http://yaml.org/) format and feature three
top level keys: services, volumes, and networks. Each service in the services section defines a 
separate docker container with a configuration which is independent of other services.

### Deploying
1.You need to clone the repository.

`$git clone https://github.com/lut1k/DIY_blog.git`

2.To run the app, `docker` and `docker-compose` must be installed on your system. For installation
instructions refer to the Docker [docs](https://docs.docker.com/compose/install/). 

3.The app can be run in development mode using Django's built in web server simply by executing:

```bash
cd DIY_blog
docker-compose up -- build
```

To remove all containers in the cluster use:

```bash
docker-compose down
```

4.After starting the application in Docker, the port are open: 8000 - `DIY_blog`.