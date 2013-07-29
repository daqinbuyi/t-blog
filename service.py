

class Service():
    def get_articles(self, limit=5, offset=0):
        base_sql = "SELECT * FROM posts ORDER BY post_time DESC LIMIT %d OFFSET %d"
        return self.db.query(base_sql % (offset, limit))

    def get_tags_by_article_id(self, article_id):
        base_sql = "SELECT * FROM tags INNER JOIN post_tag_map ON tags.id = post_tag_map.tag_id WHERE post_tag_map.post_id = %d"
        return self.db.query(base_sql % article_id)

    def get_all_tags(self):
        base_sql = "SELECT * FROM tags"
        return self.db.query(base_sql)

    def get_recent_aricles_title(self):
        base_sql = "SELECT title FROM posts ORDER BY post_time DESC LIMIT 5"
        return self.db.query(base_sql)
