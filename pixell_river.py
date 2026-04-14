from flask import Flask, request, jsonify
import sqlite3
import os
import pickle
import hashlib
import requests
import subprocess
import yaml

app = Flask(__name__)

SECRET_KEY = "hardcoded-secret-key"
DB_PASSWORD = "P@ssw0rd123"

def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def get_db():
    return sqlite3.connect("users.db")

conn = get_db()
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    role TEXT
)
""")
conn.commit()

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = weak_hash(data.get("password"))
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    user = cursor.execute(query).fetchone()
    if user:
        return jsonify({"status": "logged in", "user": username})
    return jsonify({"status": "failed"}), 401

@app.route("/admin")
def admin():
    return jsonify({"secret": "admin-only data"})

@app.route("/user/<user_id>")
def get_user(user_id):
    user = cursor.execute(f"SELECT * FROM users WHERE id = {user_id}").fetchone()
    return jsonify({"user": user})

@app.route("/debug")
def debug():
    raise Exception("Debug info leak!")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    data = file.read()
    obj = pickle.loads(data)
    return jsonify({"loaded": str(obj)})

@app.route("/fetch")
def fetch_url():
    url = request.args.get("url")
    response = requests.get(url)
    return response.text

@app.route("/add_balance", methods=["POST"])
def add_balance():
    amount = request.json.get("amount")
    user = request.json.get("user")
    return jsonify({"message": f"Added {amount} to {user}'s balance"})

@app.route("/silent_fail")
def silent_fail():
    try:
        1 / 0
    except:
        pass
    return "Nothing to see here"

@app.route("/calc")
def calc():
    expr = request.args.get("expr")
    return str(eval(expr))

@app.route("/run")
def run():
    cmd = request.args.get("cmd")
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return output.stdout

@app.route("/read")
def read():
    path = request.args.get("path")
    with open(path, "r") as f:
        return f.read()

@app.route("/yaml")
def load_yaml():
    data = request.args.get("data")
    obj = yaml.load(data, Loader=yaml.FullLoader)
    return str(obj)

if __name__ == "__main__":
    app.run(debug=True)


