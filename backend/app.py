from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
db = client.geminidevops

@app.route("/")
def index():
  return "Merhaba Dünya!"

@app.route("/servers", methods=["GET", "POST"])
def servers():
  if request.method == "GET":
    servers = db.servers.find({})
    return {"servers": list(servers)}
  elif request.method == "POST":
    data = request.get_json()
    server = db.servers.insert_one(data)
    return {"server": server.inserted_id}

if __name__ == "__main__":
  app.run()
