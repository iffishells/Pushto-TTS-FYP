from flask import Flask ,render_template , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)

# i removed the slash from before the tmp becuase i want to create
# database on local
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

db= SQLAlchemy(app)    

class Todo(db.Model):

    sno = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime ,default=datetime.utcnow)


    def __repr__(self)->str:
        return f"{self.sno} - {self.title})"
@app.route("/" , methods=["GET", "POST"])
def hello_world():

    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        
        todo = Todo(title = title, desc=desc)
        db.session.add(todo)
        db.session.commit() 

    allTodo = Todo.query.all()
    return render_template('Index.html' ,allTodo = allTodo)

@app.route('/show')
def product():
    allTodo = Todo.query.all()
    print(allTodo)
    return "This is product page"

if __name__ == "__main__":
    app.run(debug=True) # debug true mean view error in browers 
                        # can also change the port by passing port paramter in app.run(port=8080)