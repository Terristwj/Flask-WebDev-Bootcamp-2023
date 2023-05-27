from flask import Flask, render_template

# Creates a Flask App (Object)
# __name__ is a unique name for this file
app = Flask(__name__)

# WebApp starting URL
@app.route("/")
def App():
    '''WebApp starts here'''
    
    kwargs = {
        "name": "John Doe",
        "intro": "Greetings!",
        "hobbies": ["Gaming", "Programming", "Procastinating", "Standup meeting", "Sleeping"],
    }

    return render_template("home.html", **kwargs)