from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")


def homepage(): 

    return render_template("index.html")


@app.route("/portfolio")


def contato():
    return render_template("portfolio.html")

    

@app.route("/curriculum")


def quemsomos():
    return render_template("curriculum.html")

if __name__ == "__main__":

    app.run(debug=True)