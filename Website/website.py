from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page01')
def page01():
    return render_template("page01.html")

@app.route('/page02')
def page02():
    return render_template("page02.html")

if __name__=="__main__":
    app.run(debug=True)
