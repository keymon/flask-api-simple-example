from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/someapi')
def someapi():
    return jsonify({"some_value": 1})
