from flask import Flask, render_template

# Creates a Flask App (Object)
# __name__ is a unique name for this file
app = Flask(__name__)

@app.route("/")


def hello():
    return render_template("index.html")