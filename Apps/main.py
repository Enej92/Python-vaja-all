import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    text ="Message from python."
    year = datetime.datetime.now().year
    return render_template("index.html", some_text=text, current_year=year)

@app.route("/")
def about():
    person = {"name": "bor", "age": 30}
    hobbies = ["basketball, family, hiking, rining"]
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(use_reloader=True)
