from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    
    conn = sqlite3.connect("club.db")
    rows = conn.execute("SELECT * FROM fixtures ORDER BY date").fetchall()
    conn.close()
    return render_template("index.html", fixtures=rows)

@app.route("/fixture/new", methods=["GET", "POST"])
def new_fixture():
    if request.method == "POST":
        conn = sqlite3.connect("club.db")
        conn.execute(
            "INSERT INTO fixtures (opponent, date, location) VALUES (?, ?, ?)",
            (request.form["opponent"], request.form["date"], request.form["location"])
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    return render_template("new.html")

@app.route("/fixture/<int:fixture_id>")
def fixture(fixture_id):
    conn = sqlite3.connect("club.db")
    f = conn.execute("SELECT * FROM fixtures WHERE id = ?", (fixture_id,)).fetchone()     
    responses = conn.execute("SELECT player_name, status FROM responses WHERE fixture_id = ?", (fixture_id,)).fetchall()  
    conn.close()
    return render_template("fixture.html", f=f, responses=responses)

@app.route("/fixture/<int:fixture_id>/respond", methods=["POST"])
def respond(fixture_id):
    conn = sqlite3.connect("club.db")
    conn.execute(
        "INSERT INTO responses (fixture_id, player_name, status) VALUES (?, ?, ?) " \
        "ON CONFLICT(fixture_id, player_name) DO UPDATE SET status = excluded.status",                                    
        (fixture_id, request.form["player_name"], request.form["status"]),              
    )
    conn.commit()                          
    conn.close()
    return redirect(url_for("fixture", fixture_id=fixture_id))