import flask
import database
from flask import Flask

app = Flask(__name__)


@app.route("/create/<username>/<password>/")
def create(username, password):
    if database.register_user(username, password):
        return f"{username}"
    else:
        return False


@app.route("/auth/<username>/<password>")
def auth(username, password):
    return str(database.authenticate_user(username, password))


if __name__ == "__main__":
    app.run(debug=True)
