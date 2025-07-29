def update_score(username, level, moves, time_taken):
    # Placing the import here to prevent circular import issues
    from server import db, ScoreMoves, ScoreTime 


    # Update ScoreMoves if it does not exist or the new moves are better (lower amount)
    existing_move_score = ScoreMoves.query.filter_by(username=username, level=level).first()
    if not existing_move_score or moves < existing_move_score.moves:
        if existing_move_score:
            existing_move_score.moves = moves
            existing_move_score.time_taken = time_taken
        else:
            db.session.add(ScoreMoves(username=username, level=level, moves=moves, time_taken=time_taken))

    # Update ScoreTime, if it does not exist or the new time is better (lower)
    existing_time_score = ScoreTime.query.filter_by(username=username, level=level).first()
    if not existing_time_score or time_taken < existing_time_score.time_taken:
        if existing_time_score:
            existing_time_score.moves = moves
            existing_time_score.time_taken = time_taken
        else:
            db.session.add(ScoreTime(username=username, level=level, moves=moves, time_taken=time_taken))

    db.session.commit()