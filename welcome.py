from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to My Flask App!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
