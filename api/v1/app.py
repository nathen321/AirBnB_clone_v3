#!/usr/bin/python3
"""
It's time to start MY API!
"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    storage.close()



if __name__ == "__main__":
    try:
        host = os.environ.get('HBNB_API_HOST')
    except:
        host = '0.0.0.0'
    try:
        port = os.environ.get('HBNB_API_PORT')
    except:
        port = '5000'

    app.run(host=host, port=port, threaded=True)
