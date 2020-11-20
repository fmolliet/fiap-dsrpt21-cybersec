import json
import os
from flask import Flask, request, jsonify
import importlib

from PastebinCrawler       import PasteBin
from HaveibeenpwnedCrawler import HaveIbeenPwed 
from crawler               import GoogleCrawler

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/search',  methods=["POST"])
def search():
    try:
        res   = request.json
        tipo  = res['type']
        query = res['query']
        return jsonify(GoogleCrawler().search(tipo, query))
    except:
        return jsonify( {"code": 500, "message": "Erro inesperado" })

@app.route("/pastebin", methods=["GET"])
def pastebin():
    return PasteBin().crawlRaw('ubB4qbH6')
    
    
@app.route("/haveibeen", methods=["GET"])
def haveibeenpwned():
    try:
        return HaveIbeenPwed().crawlJson('teste@teste.com')
    except:
        return None
    

if __name__ == '__main__':
    app.run()
    