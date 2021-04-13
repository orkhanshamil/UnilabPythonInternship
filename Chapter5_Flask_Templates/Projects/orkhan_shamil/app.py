from flask import Flask, render_template , url_for

app = Flask(__name__)

pages = (
    ("Home","home"),
    ("About","about"),
    ("Image","img"),
    ("Video", "video")
)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html",  pages = pages)
@app.route('/img')
def img():
    return render_template("img.html",  pages = pages)
@app.route('/video')
def video():
    return render_template("video.html",  pages = pages)


if __name__ == '__main__':
    app.run(port=8085, debug=True)