from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>This is Jenkins CI CD pipeline.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
