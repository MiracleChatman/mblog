from flask import Flask, render_template, request, redirect, url_for, flash
from peewee import *
import sqlite3

conn = sqlite3.connect('post')
cur = conn.cursor()

posts ='''CREATE TABLE POST(
   blogname CHAR(225) NOT NULL,
   content TEXT(),
   author CHAR(225),
)'''
cur.execute('posts')
cur.execute('''INSERT INTO POST( blogname, content, author) VALUES  ('the best post', 'this is my first blog post', 'miracle')''')
conn.commit()


app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods = ['POST'])
def add_post():
    if request.method == 'POST':
        flash("Data Inserted Successfully")
        blogname = request.form['blogname']
        content = request.form['content']
        author= request.form['author']
        Post.create()

        return redirect(url_for('Index'))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.debug=True
    initialize()
    app.run()
