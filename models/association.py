
#sqlalchemy imports
from sqlalchemy import Column, Integer, ForeignKey, Table

#local imports
from database import db

post_tags = Table(
    "post_tag_map",
    db.Model.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")))
