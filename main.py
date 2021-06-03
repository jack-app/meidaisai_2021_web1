from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shikiso")
def shikisoshikiso():
    return render_template("akaishikiso.html")

@app.route("/tweet")
def tweet():
    return render_template("tweet.html")

if __name__ == "__main__" :
    app.run(debug=True,threaded=True)
