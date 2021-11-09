## Technical Test

### Django Menu Manager Launch Instructions

> To start the project, Docker is recommended. The follow instructions explain how to start the project using docker.

We have 3 services:
- Database
- Back
- Front

1. First, we have to configurate the environment variables. In the docker compose, where is the back service, you can find environment section:
```
environment:
    DB_NAME: 'db_test'
    DB_HOST: 192.168.1.xx
    DB_USERNAME: 'root'
    DB_PASSWD: 'thepassis1'
```

Replace this variables with the custom configuration.

After that, you use the next command:
``` docker-compose up ``` or ``` docker-compose up -d```. This will start the three containers.

2. **Run the unit testing**:
To run the unit tests, you should connect to the *cont_back* container. You can do it with the next instruction: ```docker exec -it cont_back sh```. Inside the container, you can run the next instructions:
```python manage.py test```.
It will run the unit testing.

3. **Authentication or django admin**: You can open the django admin and it has by default the next user:
```
user: admin
passwd: admin
```

#### Notes:
- Back container was developed in python3.9 with django3.2, djongo for mongo db and djangorestframework for api
- Front container was developed in react, with chakra ui for the interface.