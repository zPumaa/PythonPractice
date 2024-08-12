from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(blog_url)
blog_data = response.json()

@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)

@app.route('/about')
def about():
    return render_template("about.html", blogs=blog_data)

@app.route('/contact')
def contact():
    return render_template("contact.html", blogs=blog_data)

@app.route('/blog/<blog_num>')
def view_blog(blog_num):
    blog = blog_data[int(blog_num) - 1]
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)