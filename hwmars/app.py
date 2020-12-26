from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<username>')
def hello_user(username):
    return f'Hello {username}'


@app.route('/health')
def health_checking():
    ret = {'status': 'UP'}
    return jsonify(ret)


if __name__ == '__main__':
    app.run(port=5000, debug=False)

