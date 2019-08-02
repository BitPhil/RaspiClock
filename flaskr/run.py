from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def alarms():
    return render_template('alarms.html')

def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')