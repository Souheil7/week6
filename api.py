	
from flask import flask 
import requests
import json
from flask import request, jsonify

app = Flask(__name__)


app.config["DEBUG"] = True

data = {
    'course': 411,
    "courseName": "Software in Telecommunications",
    "releaseYear": 2021,
    "courseActive": True,
    "droppedStudents": None,
    "date": "12/10/2021",
    "someData": [[11, 2], [22, 4], [33, 1], [44, 5]],
    "scores": {"a": 77, "b": 46, "c": 91}
    }


@app.route('/',methods=['GET'])
def data_all():
    return jsonify(data)


@app.route('/scores',methods=['GET'])
def data_scores():
    return jsonify(data['scores'])


@app.route('/scores/<int:number>', methods=['GET'])
def get_score(number):
    n = list(data['scores'])[number]

    try: 
        return jsonify({list(data["scores"])[number]: (data["scores"])[n]})

    except: 
        return "Nothing"
