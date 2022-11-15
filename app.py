from flask import Flask, Markup, render_template
from turbo_flask import Turbo

from rm2svg import rm2svg

import threading, random, time

app = Flask(__name__)
turbo = Turbo(app)

@app.context_processor
def inject_load():
    svg = rm2svg(r"/home/root/local/share/remarkable/xochitl/8b3e8d9b-2bb5-429a-ab5f-6ca89a50ef1f/86bdb7f5-3477-4815-a877-9083118c01fa.rm")
    return {'load1': Markup(svg), 'load5': random.randint(1,100), 'load15': random.randint(1,100)}

@app.route('/')
def index():
    return render_template('index.html')

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(0.2)
            print("checking for changes")
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))

