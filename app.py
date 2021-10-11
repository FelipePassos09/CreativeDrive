from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return app.render_template('index.html')
