from flask import Flask, render_template, request, redirect, session
from models import db, User, Question
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "kodland_secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if not os.path.exists('database.db'):
    with app.app_context():
        db.create_all()

# Ana sayfa
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        session['user_id'] = user.id
        return redirect('/quiz')
    return render_template('index.html')

# Quiz sayfası
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    user = User.query.get(session.get('user_id'))
    questions = Question.query.limit(5).all()

    if request.method == 'POST':
        score = 0
        for q in questions:
            answer = request.form.get(str(q.id))
            if answer == q.correct_answer:
                score += 1
        user.last_score = score
        user.highest_score = max(user.highest_score, score)
        db.session.commit()
        return redirect('/result')

    return render_template('quiz.html', questions=questions, user=user)

# Sonuç sayfası
@app.route('/result')
def result():
    user = User.query.get(session.get('user_id'))
    top_score = db.session.query(db.func.max(User.highest_score)).scalar()
    return render_template('result.html', user=user, top_score=top_score)


if __name__ == '__main__':
    app.run(debug=True)
