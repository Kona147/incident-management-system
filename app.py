from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database/incidents.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Open'
        )
    ''')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database/incidents.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents")
    incidents = cursor.fetchall()
    conn.close()
    return render_template('index.html', incidents=incidents)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        conn = sqlite3.connect('database/incidents.db')
        conn.execute("INSERT INTO incidents (title, description) VALUES (?, ?)", (title, description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create_incident.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    conn = sqlite3.connect('database/incidents.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        status = request.form['status']
        cursor.execute("UPDATE incidents SET status = ? WHERE id = ?", (status, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM incidents WHERE id = ?", (id,))
    incident = cursor.fetchone()
    conn.close()
    return render_template('update_incident.html', incident=incident)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
