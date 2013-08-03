#coding:utf8
import os

#site settings
site_options = dict(
    site_name="Justfly's Blog",
    subtitle="a web developer, loves pyton and go",
    author="Justfly He",
    description="我的个人技术博客，关注python和go语言！",
    keywords=["python", "go"],
    password="pengfei1018",
    index_page_size=5,
    archive_page_size=20,
    navs=[
        dict(name="Home", link="/"),
        dict(name="Archive", link="/archive"),
        dict(name="About", link="/about"),
    ],
    copyright="Justfly He",
    duoshuo_shortname="justflyBlog",
    theme="modernist"
)

#system settings
DEBUG = True
COOKIE_SECRET = "justfly"

#database settings
if "SERVER_SOFTWARE" in os.environ:
    import sae.const
    DATABASE_URI = "mysql://%s:%s@%s:%s/%s?charset=utf8" % (
        sae.const.MYSQL_USER,
        sae.const.MYSQL_PASS,
        sae.const.MYSQL_HOST,
        sae.const.MYSQL_PORT,
        sae.const.MYSQL_DB
    )
    DATABASE_ECHO = False
else:
    DATABASE_URI = "sqlite:///db/data.db"
    DATABASE_ECHO = True
