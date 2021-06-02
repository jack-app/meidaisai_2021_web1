from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shikiso")
def shikisoshikiso():
    name = request.args.get("name")
    return render_template("akaishikiso.html")

@app.route("/shikiso",methods=["post"])
def post():
    name = request.args.get("name")
    return render_template("akaishikiso.html",name=name)

if __name__ == "__main__" :
    app.run(debug=True,threaded=True)
    