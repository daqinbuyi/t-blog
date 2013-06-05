from database import db
import post

print 'haha'
db.create_tables()

my_post1 = post.Post("test1 post")
my_post2 = post.Post("test2 post")
post.save(my_post1)
post.save(my_post2)
db.session.commit()