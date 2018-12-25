from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1> This is Fabian </h1>"

@app.route("/chess")
def chess():
    return render_template("chess.html")


if __name__ == "__main__":
    app.run(debug=True)