import os
import datetime
import pytz

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/time")
def time():
    berlin_tz = pytz.timezone("Europe/Berlin")
    berlin_time = datetime.datetime.now(berlin_tz)
    return berlin_time.strftime("%d.%m.%Y, %H:%M:%S Uhr")

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
