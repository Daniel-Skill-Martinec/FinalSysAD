from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reservations.html', methods=['GET', 'POST'])
def reservations():
    if request.method == 'POST':
        name = request.form["name"]
        arriving = request.form["arriving"]
        departing = request.form["departing"]

        cmd = "INSERT INTO reserved (name, arriving, departing) VALUES ('{0}', '{1}', '{2}')".format(name, arriving, departing)

        with sql.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()

        return redirect(url_for('confirmation', name=name, arriving=arriving, departing=departing))
    else:
        return render_template('reservations.html')
    
@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    arriving = request.args.get('arriving')
    departing = request.args.get('departing')

    return render_template('confirmation.html', name=name, arriving=arriving, departing=departing)

@app.route('/roomlist.html')
def roomlist():
    conn = sql.connect('database.db')
    conn.row_factory = sql.Row

    cmd = "SELECT * FROM reserved"
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template('roomlist.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)