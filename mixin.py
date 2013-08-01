from model import Post, Category, Tag, post_tag


class BaseMixin(object):

    def _add_filters(self, T, rc, **kwargs):
        '''
        {
            "key": "value",
            "join": [(AA.bbs, BB.key == value), ()]
        }
        '''
        if "join" in kwargs:
            for (model, exp) in kwargs["join"]:
                rc = rc.join(model)
                rc = rc.filter(exp)
            del kwargs["join"]
        for (key, value) in kwargs.items():
            if not hasattr(T, key):
                continue
            rc = rc.filter(getattr(T, key) == value)
        if "limit" in kwargs:
            rc = rc.limit(kwargs["limit"])
        if "offset" in kwargs:
            rc = rc.limit(kwargs["offset"])
        return rc

    def get_one(self, T, **kwargs):
        rc = self.db.query(T)
        rc = self._add_filters(T, rc, **kwargs)
        return rc.one()

    def get_model_list(self, T, *cols, **kwargs):
        if cols:
            query_list = [getattr(T, col) for col in cols if hasattr(T, col)]
            rc = self.db.query(*query_list)
        else:
            rc = self.db.query(T)
        rc = self._add_filters(T, rc, **kwargs)
        return rc.all()

    def count(self, T, **kwargs):
        rc = self.db.query(T)
        rc = self._add_filters(T, rc, **kwargs)
        return rc.count()

    def insert(self, model):
        self.db.add(model)
        self.db.commit()

    def insert_many(self, models):
        self.db.add_all(models)
        self.db.commit()

    def update(self, T, data, **kwargs):
        rc = self.db.query(T)
        rc = self._add_filters(T, rc, **kwargs)
        rc.update(data)
        self.db.commit()

    def delete(self, T, data, **kwargs):
        rc = self.db.query(T)
        rc = rc._add_filters(T, rc, **kwargs)
        rc.delete()
        self.db.commit()


class PostMixin(object):
    def count_posts(self, category_name=None):
        my_query = self.db.query(Post).join(Post.category)
        if category_name:
            my_query = my_query.filter(Category.name == category_name)
        return my_query.count()

    def get_posts(self, category_name=None, tag_name=None, page=1):
        my_query = self.db.query(Post)
        if category_name:
            my_query = my_query.join(
                Category,
                Post.category_id == Category.id)
            my_query = my_query.filter(Category.name == category_name)
        if tag_name:
            my_query = my_query.\
                join(post_tag, Post.id == post_tag.post_id).\
                join(Tag, post_tag.tag_id == Tag.id)
            my_query = my_query.filter(Tag.name == tag_name)
        start, end = self._get_start_end(page)
        return my_query.order_by(Post.id.desc())[start:end]

    def get_recent_posts(self):
        return self.db.\
            query(Post.id, Post.title).\
            order_by(Post.post_time.desc())[:5]

    def get_headers(self, category_id=None, page=1):
        my_query = self.db.query(
            Post.id,
            Post.title,
            Category.name,
            Post.post_time).join(Post.category)
        if category_id:
            my_query = my_query.filter(Post.category_id == category_id)
        start, end = self._get_start_end(page)
        return my_query.order_by(Post.id.desc())[start: end]
