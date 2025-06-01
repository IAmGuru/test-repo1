from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellow_world():
    return "Hellow World !!"

if __name__ == '__main__':
    app.run(debug=False, host='localhost', port=5000)
