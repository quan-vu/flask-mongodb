from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mytest"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    online_users = None
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)