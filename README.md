# Mosquitto Firebase Auth

This is an auth plugin for [Mosquitto](https://github.com/eclipse/mosquitto) which uses [mosquito_pyauth](https://github.com/jasper-lyons/mosquitto_pyauth) to load a python module which uses the [firebase_admin](https://github.com/firebase/firebase-admin-python) library to authenticate users submitting messages to mosquitto instance via Google Firebase.

## Getting started.

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

## Authenticating with mosquitto-firebase-auth

You will need to pass the JWT provided by the firebase authentication api into the `password` of a mqtt connection. You can put what ever information you like into the `username` field, it is unused though it seems handy to identify your users when connecting with it!

## Notes:
1. We're not handling Access Controll Lists (ACL's) at all in this plugin yet. You'll want to make some changes to the `mosquitto/mosquitto_firebase_auth.py` file if you need them.
2. I have no idea what `def psk_key_get(identity, hint)` does so it currently does nothing.
