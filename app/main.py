# -*- coding: utf-8 -*-

import webbrowser

from flask import Flask ,render_template  
app = Flask(__name__) 
@app.route('/')
def index():
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=dashcam+russia")
   
    return render_template('base.html')



 
