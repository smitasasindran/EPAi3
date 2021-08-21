from flask import Flask
from flask import jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def root():
    print('test')
    # return {'statusCode': 200, 'data': "Greetings, Earthlings!"}
    return "<title> Smita Sasindran </title> <p>Greetings, Earthlings!</p>"

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=9000)
