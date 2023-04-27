from flask import Flask, url_for, redirect, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternew")
def roomlist():
    return render_template("roomlist.html")

@app.route("/addrec", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        name = request.form["name"]
        arrival = request.form["arrival"]
        departure = request.form["departure"]

        cmd = "INSERT INTO students (name, arrival, departure) VALUES ('{0}', '{1}', '{2}')".format(name, arrival, departure)

        with sql.connect("databse.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            msg = "Inserted"
            return render_template("output.htm", msg = msg)

if __name__ == "__main__":
    app.run(debug=True)
        