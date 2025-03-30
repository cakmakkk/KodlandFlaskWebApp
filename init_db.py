from app import app, db
from models import Question

with app.app_context():
    db.drop_all()
    db.create_all()

    sample_questions = [
        Question(
            topic="Discord.py",
            question_text="What is the main purpose of discord.py library?",
            option_a="Data analysis",
            option_b="Web development",
            option_c="Discord bot development",
            option_d="GUI applications",
            correct_answer="C"
        ),
        Question(
            topic="Flask",
            question_text="Which command starts the Flask development server?",
            option_a="flask run",
            option_b="python manage.py",
            option_c="flask start",
            option_d="run flask",
            correct_answer="A"
        ),
        Question(
            topic="AI",
            question_text="Which library is commonly used for machine learning?",
            option_a="Flask",
            option_b="NumPy",
            option_c="scikit-learn",
            option_d="Django",
            correct_answer="C"
        ),
        Question(
            topic="Computer Vision",
            question_text="Which library is used for object detection?",
            option_a="NLTK",
            option_b="ImageAI",
            option_c="Requests",
            option_d="Tkinter",
            correct_answer="B"
        ),
        Question(
            topic="NLP",
            question_text="What does NLTK stand for?",
            option_a="Natural Learning Toolkit",
            option_b="Natural Language Toolkit",
            option_c="Natural Language Terminal Kit",
            option_d="Natural Learning Test Kit",
            correct_answer="B"
        )
    ]

    db.session.add_all(sample_questions)
    db.session.commit()
    print("Sample data inserted.")

