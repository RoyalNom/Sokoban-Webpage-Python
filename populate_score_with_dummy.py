from server import db, app, ScoreMoves, ScoreTime

with app.app_context():
    dummy_scores_moves = [
        ScoreMoves(username='Alice', level='1', moves=20, time_taken=20),
        ScoreMoves(username='AlexRoyal', level='1', moves=30, time_taken=19),
        ScoreMoves(username='BramBoter', level='2', moves=25, time_taken=40),
        ScoreMoves(username='CharlieBrown', level='2', moves=30, time_taken=30),
        ScoreMoves(username='DiamondDiana', level='3', moves=40, time_taken=60),
        ScoreMoves(username='EveLol', level='3', moves=50, time_taken=72),
        ScoreMoves(username='FrankieFrog', level='4', moves=60, time_taken=80),
        ScoreMoves(username='GinaGiraffe', level='4', moves=80, time_taken=110),
    ]

    dummy_scores_time = [
        ScoreTime(username='Alice', level='1', moves=20, time_taken=20),
        ScoreTime(username='AlexRoyal', level='1', moves=30, time_taken=19),
        ScoreTime(username='BramBoter', level='2', moves=25, time_taken=40),
        ScoreTime(username='CharlieBrown', level='2', moves=30, time_taken=30),
        ScoreTime(username='DiamondDiana', level='3', moves=40, time_taken=60),
        ScoreTime(username='EveLol', level='3', moves=50, time_taken=72),
        ScoreTime(username='FrankieFrog', level='4', moves=60, time_taken=80),
        ScoreTime(username='GinaGiraffe', level='4', moves=80, time_taken=110),
    ]

    db.session.bulk_save_objects(dummy_scores_moves)
    db.session.bulk_save_objects(dummy_scores_time)
    db.session.commit()

    print("Dummy scores for both fewest moves and score time populated successfully.")