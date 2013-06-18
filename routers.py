from handlers import index, post, admin, category, tag, about

#system routes
route = [
    (r"/", index.IndexHandler),
    (r"/post/([0-9]+)", post.ShowPostHandler),
    (r"/admin", admin.IndexHandler),
    (r"/admin/add_post", post.AddPostHandler),
    (r"/admin/posts", post.ListPostHandler),
    (r"/admin/post/edit/([0-9])+", post.EditHandler),
    (r"/admin/categories", category.IndexHandler),
    (r"/admin/tags", tag.IndexHandler),
    (r"/admin/category/edit/([0-9]+)", category.EditHandler),
    (r"/admin/category/delete/([0-9]+)", category.DeleteHandler),
    (r"/admin/tag/edit/([0-9]+)", tag.EditHandler),

    (r"/about", about.IndexHandler)
]
