from peewee import *

db= SqliteDatabase('post.db')

class Post(Model):
    blog_title = CharField(max_length=225, unique= True),
    content= TextField(),
    author = CharField(max_length=225)

    class Meta:
        database= db 

posts = [
    {"blog_title" : 'the best post',
     'content' : 'this is my first blog post',
     'author' : 'miracle' },
  { 'blog_title' : 'the worst post',
  'content' : 'this is my next blog post',
  'author' : 'miraclec' },
  ]
def add_posts():
    for post in posts:
        try:
	        Post.create(blog_title=post['blog_title'], content= post['content'], author=post['author'])
        except IntegrityError:
            post_record = Post.get(blog_title =post['blog_title'])
            post_record.content= post['content']
            post_record.author= post['author']
            post_record.save()


if __name__ == '__main__':
    db.connect()
    db.create_tables([Post], safe=True)