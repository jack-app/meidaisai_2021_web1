from flask import Flask,render_template
from db.database import init_db
from db.models import Tweet

app = Flask(__name__)

@app.route("/")
def index():
    tweets = Tweet.all()
    return render_template("index.html",tweets=tweets)

@app.route("/shikiso")
def shikisoshikiso():
    name = request.args.get("name")
    return render_template("akaishikiso.html")

@app.route("/tweet")
def tweet():
    return render_template("tweet.html")

@app.route("/shikiso",methods=["post"])
def post():
    name = request.args.get("name")
    return render_template("akaishikiso.html",name=name)

if __name__ == "__main__" :
    init_db()
    app.run(host="0.0.0.0", debug=True,threaded=True)
