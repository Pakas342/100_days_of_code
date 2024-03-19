from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_request = requests.get(blog_url)
    blog_request.raise_for_status()
    blog_data = blog_request.json()
    return render_template("index.html", blogs=blog_data)


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_request = requests.get(blog_url)
    blog_request.raise_for_status()
    blog_data = blog_request.json()[blog_id-1]
    title = blog_data['title']
    subtitle = blog_data['subtitle']
    body = blog_data['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
