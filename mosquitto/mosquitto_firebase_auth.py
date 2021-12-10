import os
from mosquitto_auth import log, LOG_INFO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

def plugin_init(opts):
    log(LOG_INFO, 'firebase auth: starting up!')
    firebase_admin.initialize_app(credentials.Certificate(os.environ.get(
        'FIREBASE_SERVICE_ACCOUNT_PATH',
        '/etc/mosquitto/.firebase-service-account.json'
    )))

def unpwd_check(username, password):
    try:
        auth.verify_id_token(password)
        return True
    except auth.RevokedIdTokenError:
        log(LOG_INFO, f"{username}'s token was revoked!")
    except auth.UserDisabledError:
        log(LOG_INFO, f"{username} has been disabled!")
    except auth.InvalidTokenError:
        log(LOG_INFO, f"{username} provided an invalid token!")
    return False

def acl_check(client_id, username, topic, access, payload):
    return True

def psk_key_get(identity, hint):
    return ''
