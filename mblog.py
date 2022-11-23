from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from peewee import *

app = Flask(__name__)
con = sqlite3.connect('blogpost.db')
con.close
app.secret_key = 'many random bytes'


@app.route('/')
def Index():
    con=sqlite3.connect('blogpost.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Blogposts")
    rows = cur.fetchall()
    return render_template('index.html', rows=rows)

@app.route('/insert', methods = ['POST'])
def add_post():
    if request.method == 'POST':
        blogname = request.form['blogname']
        content = request.form['content']
        author= request.form['author']
        with sqlite3.connect('blogpost.db') as con:
            cur = con.cursor()
            cur.execute("INSERT into Blogposts (blogname, content, author) VALUES (?,?,?)",(blogname, content, author))
            con.commit()
            flash("Data Inserted Successfully")
        return redirect(url_for('Index'))
        con.close()

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    with sqlite3.connect("blogpost.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Blogposts where id = ?", (id_data,))
            flash("Record Has Been Deleted Successfully")
        except:
            flash("can't be deleted")
        finally:
            return redirect(url_for('Index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        blogname = request.form['blogname']
        content = request.form['content']
        author= request.form['author']
        with sqlite3.connect('blogpost.db') as con:
            cur = con.cursor()
            cur.execute("""UPDATE Blogposts SET blogname=?,content=?, author=? where id=?""",(blogname, content, author, id_data))
            con.commit()
            flash("Data Inserted Successfully")
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.debug=True
    app.run()
