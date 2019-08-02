from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/alarms.html')
def alarms():
    return render_template('alarms.html')

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='192.168.178.31')

