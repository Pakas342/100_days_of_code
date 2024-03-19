from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_request = requests.get(blog_url)
blog_request.raise_for_status()
blog_data = blog_request.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)


@app.route('/blog/<int:blog_id>')
def show_blog(blog_id):
    blog = blog_data[blog_id-1]
    title = blog['title']
    subtitle = blog['subtitle']
    body = blog['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
