from flask import Flask, render_template
import datetime
import water
import os

app = Flask(__name__)

def template(title="HELLO!",text=""):
    time = datetime.datetime.now()
    templateDate = {
        'title': title,
        'time' : time,
        'text' : text
        }
    return templateDate
@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/last_watered")
def check_last_watered():
    templateData = template(text = water.get_last_watered())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "Dry"
    else:
        message = "Wet"

    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2():
    water.pump_on()
    templateData = template(text = "Watered Once")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    if toggle == "ON":
        templateData = template(text = "Auto Watering On")
        os.system("python auto_water.py & ")
    else:
        templateData = template(text = "Auto Watering Off")
        os.system("pkill -f auto_water.py")
        water.pump_off()

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)