import sqlite3

import random

from flask import Flask, session, render_template, request, g

app = Flask(__name__)

app.secret_key = "DOG-4567456988-VS-CAT"


@app.route('/')
def index():
    data = get_database()
    return render_template('index.html', execute_data=data)
    #return data[0]


@app.route("/add_items", methods=["post"])
def add_items():
    return request.form["select_items"]




def get_database():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute('SELECT name FROM groceries')
        execute_data = cursor.fetchall()
        execute_data = [str(val[0]) for val in execute_data]
    return execute_data


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()












if __name__ == '__main__':
    app.run(debug=True)