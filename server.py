import json
import os
from flask import Flask, request, jsonify
import importlib


from HaveibeenpwnedCrawler import HaveIbeenPwed 
from pipeline import Pipeline

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search',  methods=["POST"])
def search():
    try:
        res   = request.json
        tipo  = res['type']
        query = res['query']
        return jsonify(Pipeline(tipo, query).struct_data())
    except:
        return jsonify( {"code": 500, "message": "Erro inesperado" })
    
@app.route("/haveibeen", methods=["GET"])
def haveibeenpwned():
    try:
        return HaveIbeenPwed().crawlJson('teste@teste.com')
    except:
        return None
    

if __name__ == '__main__':
    app.run()
    