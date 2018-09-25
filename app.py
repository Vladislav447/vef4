import json
from bottle import *
from sys import argv

@route('/')
def index():
    ioStream = open('gengi.json','r', encoding='utf-8')
    # parsing string (JSON data) to dictionary
    dData = json.load(ioStream)
    ioStream.close()
    return template('index',gogn=dData)

run(host='0.0.0.0', port=argv[1], debug=True, reloader=True)