from flask import Flask,render_template
from db.database import init_db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shikiso")
def shikisoshikiso():
    return render_template("akaishikiso.html")

if __name__ == "__main__" :
    init_db()
    app.run(host="0.0.0.0", debug=True,threaded=True)
