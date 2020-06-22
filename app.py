# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import fortunegetter
from datetime import datetime 



# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        name = request.form["formname"]
        fortune = request.form["fortune"]
        fortuneteller = fortunegetter()
        return render_template("results.html",  name=name, fortuneteller = fortuneteller)
    else:
        return render_template("index.html")
