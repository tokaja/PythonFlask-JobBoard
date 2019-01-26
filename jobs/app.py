from flask import Flask, renter_template

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return renter_template('index.html')
