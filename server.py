import json
import os
from flask import Flask, request, jsonify
import importlib

from crawler import GoogleCrawler
from pprint import pprint

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/search',  methods=["POST"])
def search():
    try:
        res   = request.json
        tipo  = res['type']
        query = res['query']
        return jsonify(GoogleCrawler().search(tipo, query))
    except:
        return jsonify( {"code": 500, "message": "Erro inesperado" })

@app.route("/teste", methods=["POST"])
def home():
    res = request.json
    return res['id']

if __name__ == '__main__':
    app.run()
    