from server import db, app, ScoreMoves, ScoreTime

with app.app_context():
    dummy_scores_moves = [
        ScoreMoves(username='Alice', level='1', moves=170, time_taken=40),
        ScoreMoves(username='AlexRoyal', level='1', moves=160, time_taken=42.4),
        ScoreMoves(username='BramBoter', level='2', moves=165, time_taken=35),
        ScoreMoves(username='CharlieBrown', level='2', moves=160, time_taken=30.1),
        ScoreMoves(username='DiamondDiana', level='3', moves=120, time_taken=27.4),
        ScoreMoves(username='EveLol', level='3', moves=111, time_taken=24),
        ScoreMoves(username='FrankieFrog', level='4', moves=170, time_taken=65.5),
        ScoreMoves(username='GinaGiraffe', level='4', moves=140, time_taken=80),
    ]

    dummy_scores_time = [
        ScoreTime(username='Alice', level='1', moves=170, time_taken=40),
        ScoreTime(username='AlexRoyal', level='1', moves=160, time_taken=42.4),
        ScoreTime(username='BramBoter', level='2', moves=169, time_taken=32),
        ScoreTime(username='CharlieBrown', level='2', moves=160, time_taken=30.1),
        ScoreTime(username='DiamondDiana', level='3', moves=120, time_taken=27.4),
        ScoreTime(username='EveLol', level='3', moves=111, time_taken=24),
        ScoreTime(username='FrankieFrog', level='4', moves=170, time_taken=65.5),
        ScoreTime(username='GinaGiraffe', level='4', moves=140, time_taken=80),
    ]

    db.session.bulk_save_objects(dummy_scores_moves)
    db.session.bulk_save_objects(dummy_scores_time)
    db.session.commit()

    print("Dummy scores for both fewest moves and score time populated successfully.")