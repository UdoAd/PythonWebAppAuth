from flask import Flask, render_template

myApp = Flask(__name__)


@myApp.route("/")
def hello_world():
  return render_template('home.html')


if __name__ == "__main__":
  myApp.run(host='0.0.0.0', debug=True)
