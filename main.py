from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def myinfo():
    return jsonify({'slackUsername': 'itzgeebee',
                    'backend': True,
                    'age': 26,
                    'bio':
                        'I am a backend developer who loves to code in Python and Javascript'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
