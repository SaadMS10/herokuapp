# -*- coding: utf-8 -*-


app = Flask(__name__) 

@app.route('/')
def index():
    return redirect("https://www.youtube.com/results?search_query=dashcam+russia", code=302)




 
