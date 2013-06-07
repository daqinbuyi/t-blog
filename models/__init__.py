
# # local imports
from database import db

import post
import tag
import category
import association

from datetime import datetime

#create tables in database
db.create_tables()

# my_post = post.Post("test title", "test content", datetime.now())
# my_post.category = category.Category("test category")
# post.add(my_post)
# db.session.commit()
