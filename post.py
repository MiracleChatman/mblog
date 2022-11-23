import sqlite3
con = sqlite3.connect('blogpost.db')
print("database opened successfully")
con.execute("create table Blogposts (id INTEGER PRIMARY KEY AUTOINCREMENT, blogname TEXT NOT NULL, content TEXT NOT NULL, author TEXT NOT NULL)")
print("table created successfully")
con.close