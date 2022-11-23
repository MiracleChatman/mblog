from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from peewee import *



app = Flask(__name__)
app.secret_key = 'many random bytes'
con = sqlite3.connect('post.db')
con.close

@app.route('/')
def Index():
    con=sqlite3.connect('post.db')
    cur = con.cursor()
    cur.execute("select * from Posts")
    data = cur.fetchall()
    return render_template('index.html', posts=data)

@app.route('/insert', methods = ['POST'])
def add_post():
    if request.method == 'POST':
        try:
            blogname = request.form['blogname']
            content = request.form['content']
            author= request.form['author']
            with sqlite3.connect('post.db') as con:
                cur = con.cursor()
                cur.execute("INSERT into Posts (blogname, content, author) VALUES (?,?,?)",(blogname, content, author))
                con.commit()
                flash("Data Inserted Successfully")
        except:
            con.rollback()
            flash("cant add the post to the list")
        finally:
            return redirect(url_for('Index'))
            con.close()

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id):

    id= request.form['id']
    with sqlite3.connect("post.db") as con:
        try:
            cur =  con.cursor()
            cur.execute("delete from Posts where id = ?",id)
            flash("Record Has Been Deleted Successfully")
            sqlite3.connect.commit()
        except: 
            flash("cant be deleted")
        finally:
            return redirect(url_for('Index'))  

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        try:
            id_data= request.form['id']
            blogname = request.form['blogname']
            content = request.form['content']
            author= request.form['author']
            with sqlite3.connect('post.db') as con:
                cur = con.cursor()
                cur.execute("update Posts set (blogname, content, author) VALUES (?,?,?)",(blogname, content, author))
                con.commit()
                flash("Data updated Successfully")
        except:
            con.rollback()
            flash("cant update the post to the list")
        finally:
            return redirect(url_for('Index'))
            con.close()
        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.debug=True
    app.run()
