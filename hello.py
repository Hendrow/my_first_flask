from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
  return "<h2>Hello, semuanya!</h2>"
