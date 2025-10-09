from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Менің Azure қосымшам жұмыс істейді!</h1>'

if __name__ == '__main__':
    app.run()
