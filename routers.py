from handlers import index, post, admin, category, tag, about

#system routes
route = [
    (r"/", index.IndexHandler),
    (r"/post/([0-9]+)", post.ShowPostHandler),
    (r"/admin", admin.IndexHandler),
    (r"/admin/add_post", post.AddPostHandler),
    (r"/admin/list_post", post.ListPostHandler),
    (r"/admin/categories", category.IndexHandler),
    (r"/admin/tags", tag.IndexHandler),

    (r"/about", about.IndexHandler)
]
