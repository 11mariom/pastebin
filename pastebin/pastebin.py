# -*- encoding: utf-8 -*-

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

from paste import Paste

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/paste/<id>")
def get_paste(id):
    p = Paste()
    return p.get(id).get_data()

@app.route("/paste/", methods = ["POST"])
def put_paste():
    data = request.get_data()
    print(data)
    p = Paste()
    return "pasted to id: %s" % (p.put(data))

def main():
    app.run()

if __name__ == "__main__":
    app.debug = True
    init_db()
    main()
