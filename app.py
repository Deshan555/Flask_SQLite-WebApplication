import sqlite3

import random

from flask import Flask, session, render_template, request, g

app = Flask(__name__)

app.secret_key = "DOG-4567456988-VS-CAT"


@app.route('/')
def index():
    data = get_database()
    #return render_template('index.html')
    return str(data)


def get_database():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM groceries')
    return cursor.fetchall()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()












if __name__ == '__main__':
    app.run(debug=True)