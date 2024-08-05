#!/usr/bin/python3
"""host and port"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def cls_engn(exception):
    """clos engen"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """error 404"""
    res = {"error": "Not found"}
    return jsonify(res), 404


if __name__ == "__main__":
    x = getenv("HBNB_API_HOST", "0.0.0.0")
    y = int(getenv("HBNB_API_PORT", 5000))
    app.run(debug=True, host=x, port=y, threaded=True)