from flask import Flask, jsonify
from tinydb import TinyDB, Query


app = Flask(__name__)
db = TinyDB('db.json')


@app.route('/')
def hello():
  return 'Hello, World!'


@app.route('/add/<name>')
def add_name(name):
  db.insert({'name': name})
  return jsonify({'status': 'ok', 'added': name})


@app.route('/list')
def list_names():
  return jsonify(db.all())


if __name__ == '__main__':
  app.run(debug=True)
