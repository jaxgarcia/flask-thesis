import os

from flask import Flask
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Jacks/Projects/flask_thesis'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER']



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/abstract')
def abstract():
    import extract, preprocess, score

    extract.output = extract.convert_pdf_to_txt("research2.pdf")
    extract.importantExtraction(extract.output)
    preprocess
    score
    return render_template("abstract.html")


if __name__ == "__main__":
    app.run()
