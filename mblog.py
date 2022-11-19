from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app.config('MySQL_HOST') = 'localhost'
app.config('MySQL_USER') = 'root'
app.config('MySQL_PASSWORD') = 'localhost'
app.config('MySQL_DB') = 'blogapplication'

mysql= MySQL(mblog)

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['blogname']
        content = request.form['content']
        author = request.form['author']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.debug=True
    app.run()
