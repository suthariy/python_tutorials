"""
using render_template to use the templates in Flask App
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def homepage():
    try:
        return render_template('index.html')
    except Exception as e:
        return(str(e))

@app.route("/about/")
def aboutpage():
    try:
        return render_template('about.html')
    except exception as e:
        return(str(e))

@app.route("/page-one/")
def pageone():
    try:
        btn_type = "info"
        name = "This is Page about Python"
        exlist = ["1.0","2.0","3.0"]
        return render_template('page-one.html',btn_type=btn_type,name =name , exlist = exlist)
    except exception as e:
        return(str(e))

@app.errorhandler(404)
def error404(e):
    return render_template("error404.html")

if __name__ == "__main__":
    app.run()
