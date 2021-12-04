from flask import Flask ,render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import pandas as pd
import numpy as np



app = Flask(__name__)

# i removed the slash from before the tmp becuase i want to create
# database on local
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

# db= SQLAlchemy(app)    

# class Todo(db.Model):

#     sno = db.Column(db.Integer , primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime ,default=datetime.utcnow)


#     def __repr__(self)->str:
#         return f"{self.sno} - {self.title})"
# @app.route("/" , methods=["GET", "POST"])

@app.route("/")
def hello_world():


    # if request.method == "POST":
    #     title = request.form["title"]
    #     desc = request.form["desc"]
        
    #     todo = Todo(title = title, desc=desc)
    #     db.session.add(todo)
    #     db.session.commit() 

    # allTodo = Todo.query.all()


    folder = 'static/Datasets'

    folder_list = []
    for name in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,name)):
            folder_list.append(name)

    speech_db = {}
    for name in folder_list:
    #     print(name)
        speech_db[name] = []

    for name in folder_list:
        for count in range(1,10):
            path = "static/Datasets/"+name+"/"+name+"-"+str(count)+".wav" 
            speech_db[name].append(path)
    
    return render_template('Index.html' ,speech_db=speech_db)
    #allTodo = allTodo)

@app.route('/speech')
def speech_database():

    folder = 'static/Datasets'

    folder_list = []
    for name in os.listdir(folder):
        if os.path.isdir(os.path.join(folder,name)):
            folder_list.append(name)

    speech_db = {}
    for name in folder_list:
    #     print(name)
        speech_db[name] = []

    for name in folder_list:
        for count in range(1,10):
            path = "static/Datasets/"+name+"/"+name+"-"+str(count)+".wav" 
            speech_db[name].append(path)

    list_keys_30 = list(speech_db.keys())[0:30]
    list_keys_60 = list(speech_db.keys())[31:60]
    list_keys_90 = list(speech_db.keys())[61:90]
    print(list_keys_30)
    return render_template('speech.html' ,speech_db=speech_db)
                            # list_keys_30=list_keys_30)
                           # list_keys_60=list_keys_60,
                            #list_keys_90=list_keys_90)

if __name__ == "__main__":
    app.run(debug=True ,port=5000) # debug true mean view error in browers 
                        # can also change the port by passing port paramter in app.run(port=8080)