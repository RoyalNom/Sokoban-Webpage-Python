from server import db, app, Score

with app.app_context():
    dummy_scores = [
        Score(username='Alice', level='1', moves=20, time_taken=20),
        Score(username='AlexRoyal', level='1', moves=30, time_taken=19),
        Score(username='BramBoter', level='2', moves=25, time_taken=40.5),
        Score(username='CharlieBrown', level='2', moves=30, time_taken=30.2),
        Score(username='DiamondDiana', level='3', moves=40, time_taken=60.5),
        Score(username='EveLol', level='3', moves=50, time_taken=72.3),
        Score(username='FrankieFrog', level='4', moves=60, time_taken=80.1),
        Score(username='GinaGiraffe', level='4', moves=80, time_taken=110.4),
    ]
    db.session.bulk_save_objects(dummy_scores) # Simpely commits the list of objects
    db.session.commit()
    print("Dummy scores populated successfully.")