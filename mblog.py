from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Miracles\'s Blog'

if __name__ == '__main__':
    app.run()