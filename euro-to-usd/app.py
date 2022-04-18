
import os

from flask import Flask
from flask import render_template, request
from currency_converter import CurrencyConverter

app = Flask(__name__)


@app.route("/")
def form():
    return render_template("form.html")




@app.route("/hello", methods=["POST"])
def my_form_post():
    username=request.form["username"]
    pwd=request.form["pwd"]	
    return render_template("hello.html",username=username)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
