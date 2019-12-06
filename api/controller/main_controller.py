import json
import sys
from collections import OrderedDict
from imp import reload

from authenticate import requires_auth
from view.idea import getIdeaForUser
from view.user import getUserById

#reload(sys)
#sys.setdefaultencoding('utf-8')

from flask import Flask, escape, request, jsonify, abort, Response, Request


app = Flask(__name__, root_path='api/')
app.config['JSON_SORT_KEYS'] = False

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route("/authenticate", methods=['POST'])
def authenticate():
    # extracting response text
    request_data = request.json
    if request_data["name"]=="irene@gmail.com" and request_data["password"] == "test" :
        data = {
            "message": "Successully Logged In!",
        }
        js = json.dumps(data)
        resp = Response(js, status=200, mimetype='application/json')
    else:
        data = {
            "message": "Incorrect Credentials!",
        }
        js = json.dumps(data)
        resp = Response(js, status=404, mimetype='application/json')

    return resp


@app.route("/generator/user/v1/<userId>", methods=['GET'])
@requires_auth
def getUser(userId):
    # extracting response text
    user_id = int(userId)
    if(user_id in (1,2)):
        return Response(getUserById(user_id).toJSON(), mimetype='application/json')
    else:
        abort(404, description="User does not exist")



@app.route("/generator/idea/v1/<userId>/<city>/<country>", methods=['GET'])
@requires_auth
def getIdea(userId,city,country):
    # extracting response text
    user_id = int(userId)
    if (user_id in (1, 2)):
        return Response(getIdeaForUser(user_id, city, country).toJSON(), mimetype='application/json')
    else:
        abort(404, description="User does not exist")


if __name__ == "__main__":
    app.run(port=80,debug=True)