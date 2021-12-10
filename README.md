# Mosquitto Firebase Auth

This is an auth plugin for [Mosquitto](https://github.com/eclipse/mosquitto) which uses [mosquito_pyauth](https://github.com/jasper-lyons/mosquitto_pyauth) to load a python module which uses the [firebase_admin](https://github.com/firebase/firebase-admin-python) library to authenticate users submitting messages to mosquitto instance via Google Firebase.

1. Pull this repository.

2. Build the [mosquitto_pyauth](https://github.com/jasper-lyons/mosquitto_pyauth) image.

3. Build the mosquitto-firebase-auth image.

  ```
  docker build . --tag mosquitto-firebase-auth
  ```

4. Generate and download a new firebase service account private key by following the "Inistialize the SDK" step [here](https://firebase.google.com/docs/admin/setup?authuser=0)
  You'll likely want to save it into the `mosquitto` directory as `.firebase-service-account.json`.

5. Run the docker container!

```
docker run -v ${PWD}/mosquitto:/etc/mosquitto -e PYTHONPATH=/etc/mosquitto -p 1883:1883 -p 1884:1884 mosquitto-firebase-auth
```

6. Run it with docker compose!

```
# docker-compose.yml
version: "3.9"
services:
  mosquitto:
    image: mosquitto-pyauth
    environment:
      - PYTHONPATH=/etc/mosquitto/
    volumes:
      - ./mosquitto:/etc/mosquitto
    ports:
      - "1883:1883"
      - "1884:1884"
```

```
docker-compose up
```
