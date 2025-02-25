# Write these in the terminal
# pip install flask
# pip install flask_sqlalchemy

from flask import Flask, render_template, request, redirect
# SQLAlchemy is Flask's ORM (object-Relational Mapper)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone 

# Create Flask app instance
app = Flask(__name__)

# Create SQLite database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db is what we are calling our database, set it up to be an instance of SQLAlchemy, and pass in our flask app
db = SQLAlchemy(app)

# define model of a to do list TASK
class Task(db.Model): 
    # db.Column is a column in the database
    # also specify the data type of that key
    # PICK ONE column to be the "primary_key"
    id = db.Column(db.Integer, primary_key=True)  # (datatype, primary_key=True)
    # set maximum characters in the string to 200 & can't have an empty string as the content (prevents typing a blank entry)
    content = db.Column(db.String(200), nullable=False)   
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
       
    # NOTE: self is similair to this (this like in java)
    # String representation of the object
    def __repr__(self):
        return f'<Task {self.id}>'
    

# Flask route for displaying all tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    # ADD new Task to database
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content)
        try: 
            db.session.add(new_task)
            db.session.commit()
            # reload page
            return redirect('/')
        except:
            return 'Error adding task to database'
    
    #tasks = Task.query.order_by()
    # SELECT all Task objects from database
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)



# Create the database instance in main method
if __name__  == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port="1117", debug=True)