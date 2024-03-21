from flask import Flask, render_template
import requests

app = Flask(__name__)

# We get the info from the blogs API
blogs_url = "https://api.npoint.io/e77a12c5c77d1f911440"
blogs_request = requests.get(blogs_url)
blogs_request.raise_for_status()
blogs_json = blogs_request.json()


def blog_index(title):
    searched_index = None
    for array_index, blog in enumerate(blogs_json):
        if blog['title'] == title:
            searched_index = array_index
    return searched_index


@app.route('/')
def index():
    return render_template("index.html", blogs=blogs_json)


@app.route('/about_us')
def about_us():
    return render_template("about.html")


@app.route('/contact')
def contact_us():
    return render_template("contact.html")


@app.route('/post/<title>')
def get_post(title):
    blog_to_show = blogs_json[blog_index(title=title)]
    return render_template("post.html", blog=blog_to_show)


if __name__ == "__main__":
    app.run(debug=True)
