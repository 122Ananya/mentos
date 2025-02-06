from flask import Flask, render_template, request, redirect, url_for, flash, session, render_template_string
from database import get_db_connection
from auth import auth_bp

app = Flask(__name__)
app.secret_key = "mentos"
app.register_blueprint(auth_bp)


# -------- Home Page --------
@app.route("/")
def index():
    return render_template("index.html", username=session.get("username"))


# -------- Mood Logging --------
@app.route("/log_mood", methods=["GET", "POST"])
def log_mood():
    if request.method == "POST":
        # Save user's mood log to DB
        pass
    return render_template("log_mood.html")


@app.route("/view_mood")
def view_mood():
    # Fetch and display logged moods from DB
    return render_template("view_mood.html")


# -------- Mood Analytics --------
@app.route("/mood_chart")
def mood_chart():
    # Generate mood trend chart
    return render_template("mood_chart.html")


# -------- Therapeutic Resources --------
@app.route("/music")
def music():
    # Fetch music recommendations based on mood
    return render_template("music.html")


@app.route("/therapy_exercises")
def therapy_exercises():
    # Fetch therapy exercises based on mood
    return render_template("therapy_exercises.html")


if __name__ == "__main__":
    app.run(debug=True)
