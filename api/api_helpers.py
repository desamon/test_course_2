from api.blog_api import BlogApi


def delete_all_posts(url):
   blog_api = BlogApi(url)
   posts = blog_api.get_user_posts()
   for post in posts["posts"]:
       blog_api.delete_post(post["id"])

