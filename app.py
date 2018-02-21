import os

from flask import Flask
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Jacks/Projects/flask_thesis'
ALLOWED_EXTENSIONS = set(['pdf'])
filename = ""

app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def set_filename(name):
    global filename
    filename = name


def get_filename():
    global filename
    return filename


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            set_filename(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('generate'))
    return render_template("abstract.html")


@app.route('/generate')
def generate():
    return render_template("generate.html")


@app.route('/abstract')
def abstract():
    import extract
    pdfFile = get_filename()
    extract.convert_pdf_to_txt(pdfFile)
    import preprocess
    preprocess.preprocessInitialize("outputextracted.txt")
    import score
    score.scoreInitialize("experimentaldictionary.txt", "title.txt", "referencedictionary.txt")

    titleTxt = open('fulltitle.txt', 'r', encoding='utf-8')
    titleStr = titleTxt.read()

    abstractTxt = open('abstract.txt', 'r', encoding='utf-8')
    abstractStr = abstractTxt.read()

    abstractDictTxt = open('abstractdictionary.txt', 'r', encoding='utf-8').read()
    abstractDict = eval(abstractDictTxt)

    wScorePercentageTxt = open('weightedscorepercentage.txt', 'r', encoding='utf-8').read()
    wScorePercentageDict = eval(wScorePercentageTxt)

    return render_template("abstract.html", abstractStr=abstractStr, titleStr=titleStr, abstractDict=abstractDict, wScorePercentageDict=wScorePercentageDict)


if __name__ == "__main__":
    app.run()
