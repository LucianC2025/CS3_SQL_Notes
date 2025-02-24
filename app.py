# Write these in the terminal
# pip install flask
# pip install flask_sqlalchemy


from flask import Flask, render_template, request, redirect
# SQLAlchemy is Flask's ORM (object-Relational Mapper)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

# Create Flask app instance
app = Flask(__name__)

# Create SQLite database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db is what we are calling our database, set it up to be an instance of SQLAlchemy, and pass in our flask app
db = SQLAlchemy(app)

#