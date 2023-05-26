from flask import Flask, render_template
from jinja2 import Template

# Creates a Flask App (Object)
# __name__ is a unique name for this file
app = Flask(__name__)

# WebApp starting URL
@app.route("/")

def App():
    '''WebApp starts here'''
    template = Template("Hello, {{ name }}")
    template.render(name="John Doe")
    
    return render_template("index.html")