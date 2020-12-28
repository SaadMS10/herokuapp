# -*- coding: utf-8 -*-
from flask import Flask ,render_template,redirect

app = Flask(__name__) 

@app.route('/')
def index():
    return redirect("https://www.youtube.com/results?search_query=dashcam+russia", code=302)




 
