from flask import Flask

app = Flask(__name__)


@app.route('/') # https://my-site.com
def greeting():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True)
