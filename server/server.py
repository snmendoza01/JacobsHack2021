from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
import json


app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    search = request.form['search']
    print("user searched for:"+ search)
    return "got the gest request"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)