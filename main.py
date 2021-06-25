from flask import Flask,render_template, request, redirect
from flask.wrappers import Request
from db.database import init_db
from db.models import Tweet

app = Flask(__name__)

@app.route("/")
def index():
    tweets = Tweet.all()
    return render_template("index.html",tweets=tweets)

@app.route("/tweet",methods=["get","post"])
def tweet():
    if request.method == 'GET':
        return render_template("tweet.html")
    elif request.method == 'POST':
        name=request.form["name"]
        content=request.form["content"]
        t = Tweet(name=name, content=content, position_x='座標X', position_y='座標Y')
        t.save() 
        return redirect('/')


if __name__ == "__main__" :
    init_db()
    app.run(host="0.0.0.0", debug=True,threaded=True)
