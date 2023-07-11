from flask import Flask

import baidu

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/chepai')
def shibie():
    return baidu.tunn()["words_result"]["number"]

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5002)
