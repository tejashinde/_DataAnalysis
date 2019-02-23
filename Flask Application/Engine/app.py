from flask import Flask , render_template
from data import Elements

app = Flask(__name__)

Elements = Elements()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/miner')
def miner():
    return render_template("miner.html" , elements = Elements)

@app.route('/minersys/<string:id>/')
def minersys(id):
    return render_template("minersys.html" , id = id)

class inStream():
    query = Strinf

if __name__ == '__main__':
    app.run(debug = True)
