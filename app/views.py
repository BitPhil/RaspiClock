from app import app
from app.models import light_states

from flask import render_template, redirect, request, flash
import requests, json

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/alarms.html')
def alarms():
    return render_template('alarms.html')

@app.route('/settings.html')
def settings():
    return render_template('settings.html')

@app.route('/_lightON', methods=["POST"])
def lightOn():
    # Setting up URL to send commands to the bulb via the hue bridge
    url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"
    data = {"on":True, "bri":200} #bri = 254 is full brightness
    response = "turned on"
    # Send the command to the bulb via hue bridge
    r = requests.put(url, json.dumps(data), timeout=5)
    return response

@app.route('/_lightOFF', methods=["POST"])
def lightOff():
    # Setting up URL to send commands to the bulb via the hue bridge
    url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"
    data = {"on":False}
    response = "turned off"
    # Send the command to the bulb via hue bridge
    r = requests.put(url, json.dumps(data), timeout=5)
    return response

@app.route('/_light', methods=["POST"])
def light():
    url = "http://192.168.178.28/api/QpwEJGEz2Vw6J6z66yj2vRhC4yruI6sMr8jOnyZe/lights/4/state"
    
    # Find out whether to turn the light on or off - curent state is tracked in DB!
    state_on = light_states.query(light_states.state_on).filter_by(name="4").first()
    if state_on == False:
        data = {"on":False}
        response = "turned off"
    else:
        data = {"on":True, "bri":200}
        response = "turned on"

    # Send the command to the bulb via hue bridge
    r = requests.put(url, json.dumps(data), timeout=5)
    # Send the response
    return response