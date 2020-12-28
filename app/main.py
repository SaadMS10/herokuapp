# -*- coding: utf-8 -*-

import webbrowser
import time
from pynput.mouse import Button, Controller
from flask import Flask ,render_template  
app = Flask(__name__) 
@app.route('/')
def index():
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=dashcam+russia")
    time.sleep(2.2)
    mouse = Controller()
    mouse.position = (500, 350)
    time.sleep(1.2)
    mouse.click(Button.left,2)
    return render_template('base.html')


 