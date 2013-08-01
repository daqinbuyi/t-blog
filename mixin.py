from sqlalchemy import joinedload


class BaseMixin(object):
    def _add_filters(self, T, rc, **kwargs):
        if "join" in kwargs:
            options = [
                joinedload(getattr(T, j))
                for j in kwargs["join"] if hasattr(T, j)
            ]
            rc = rc.options(*options)
            del kwargs["join"]
        for (key, value) in kwargs.items():
            if not hasattr(T, key):
                continue
            rc = rc.filter(getattr(T, key) == value)
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
