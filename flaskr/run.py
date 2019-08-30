from flask import Flask, render_template, redirect, url_for, request
import requests, json, time

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

@app.route('/light')
def light():
    if(request.method == 'POST'):
        status_on = request.form['status_on']

        # Setting up URL to send commands to the bulb via the hue bridge
        url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"

        # Setting up the command/data based on content of status_on (true or false)
        if(status_on == True):
            data = {"on":True, "bri":200} #bri = 254 is full brightness
        else:
            data = {"on":False}

        # Send the command to the bulb via hue bridge
        r = requests.put(url, json.dumps(data), timeout=5)
    
        #after that go back to the home page
        return redirect(url_for('index'), code=302)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='192.168.178.31')

