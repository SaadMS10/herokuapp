# -*- coding: utf-8 -*-

import webbrowser

from flask import Flask ,render_template  
app = Flask(__name__) 
@app.route('/')
def index():
    webbrowser.open("https://www.youtube.com/results?search_query=dashcam+russia")
   
    return render_template('base.html')



 
