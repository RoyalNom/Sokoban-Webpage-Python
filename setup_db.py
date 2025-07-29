from server import db, app, User, ScoreMoves, ScoreTime, Levels
from flask_login import UserMixin

# Type python setup_db.py
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")