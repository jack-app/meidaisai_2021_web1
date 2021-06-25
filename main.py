from flask import Flask,render_template, request, redirect, jsonify
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
        position_x = request.form["positionX"]
        position_y = request.form["positionY"]
        t = Tweet(name=name, content=content, position_x=position_x, position_y=position_y)
        t.save() 
        return redirect('/')

@app.route("/get_positions", methods=["get"])
def get_positions():
    positions = Tweet.get_positions()
    positions = [{"position_x": position[0], "position_y": position[1]} for position in positions]
    return jsonify({"positions": positions})

if __name__ == "__main__" :
    init_db()
    app.run(host="0.0.0.0", debug=True,threaded=True)
