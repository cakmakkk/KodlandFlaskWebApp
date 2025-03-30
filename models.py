from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    highest_score =  db.Column(db.Integer, default=0)
    last_score = db.Column(db.Integer, default=0)

class Question(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100),nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String, nullable=False)

