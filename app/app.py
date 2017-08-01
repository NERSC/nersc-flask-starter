from flask import Flask, render_template
application = Flask(__name__, static_url_path="/static")

@application.route("/")
def hello():
    return render_template("hello.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0')
