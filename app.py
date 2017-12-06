from flask import Flask
from flask import request, redirect, url_for, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/abstract')
def abstract():
    return render_template("abstract.html")

if __name__ == "__main__":
    app.run()
