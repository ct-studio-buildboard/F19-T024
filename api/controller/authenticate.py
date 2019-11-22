from functools import wraps

from flask import jsonify, request


# def check_auth(username, password):
#     print("UN:" + username + " | PW:" + password)
#     return username == "irene@gmail.com" and password == "test"

def check_auth(key):
    return key == "aXJlbmVAZ21haWwuY29tOnRlc3Q="


def authenticate():
    message = {
        'message': "Authenticate."
    }
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("X-Api-Key")
        if not auth:
            return authenticate()

        elif not check_auth(auth):
            return authenticate()
        return f(*args, **kwargs)

    return decorated