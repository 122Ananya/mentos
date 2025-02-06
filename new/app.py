import flask
import database
from flask import Flask

app = Flask(__name__)


@app.route("create/<username>/<email>/<password>/")
def create(username, email, password):
    if database.register_user(username, email, password):
        return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True)
