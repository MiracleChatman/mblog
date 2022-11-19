from peewee import *

db= SqliteDatabase('students.db')

class Post(Model):
    blog_title = CharField(max_length=225, unique=True),
    content= TextField(),
    author = CharField(max_length=225)

    class Meta:
        database= db 

if __name__ == '__main__':
    db.connect()
    db.create_tables([Post], safe=True)