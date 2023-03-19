import sqlite3

import random

from flask import Flask, session, render_template, request, g

app = Flask(__name__)

app.secret_key = "DOG-4567456988-VS-CAT"
app.config["SESSION_COOKIE_NAME"] = "MY-COOKIE-666"


@app.route("/", methods=["POST", "GET"])
def index():
    session["data"], session["random_items"] = get_database()
    return render_template('index.html', execute_data=session["data"], shopping_list=session["random_items"])
    # return data[0]


@app.route("/add_items", methods=["post"])
def add_items():
    session["random_items"].append(str(request.form["select_items"]))
    return render_template('index.html', execute_data=session["data"], shopping_list=session["random_items"])


def get_database():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('grocery_list.db')
        cursor = db.cursor()
        cursor.execute('SELECT name FROM groceries')
        execute_data = cursor.fetchall()
        execute_data = [str(val[0]) for val in execute_data]

        shopping_list = execute_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]
    return execute_data, shopping_list


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)
