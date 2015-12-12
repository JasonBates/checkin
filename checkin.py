from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/test")
def test_route():
    return "<p> This is the test endpoint </p>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
