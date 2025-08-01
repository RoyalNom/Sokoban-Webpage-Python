from server import db, app, User, ScoreMoves, ScoreTime, Levels

with app.app_context():
    # Uncomment to drop specific tables:
    # db.drop_all() 

    # Drop individual tables:
    User.__table__.drop(db.engine)
    # ScoreMoves.__table__.drop(db.engine)
    # ScoreTime.__table__.drop(db.engine)
    # Levels.__table__.drop(db.engine)

    print("Selected tables dropped.")