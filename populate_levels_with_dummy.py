from server import db, app, Levels
import json

with app.app_context():
    dummy_levels = [
        Levels(
            level_id='1',
            author='DevAnt',
            json_config=json.dumps({
                "player": [1, 1],
                "goals": [3, 3],
                "boxes": [2, 1],
                "paths": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
            })
        ),
        Levels(
            level_id='2',
            author='DevAnt',
            json_config=json.dumps({
                "player": [1, 2],
                "goals": [3, 2],
                "boxes": [2, 1],
                "paths": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
            })
        ),
        Levels(
            level_id='3',
            author='DevAnt',
            json_config=json.dumps({
                "player": [0, 0],
                "goals": [2, 3],
                "boxes": [2, 1],
                "paths": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
            })
        ),
        Levels(
            level_id='4',
            author='DevAnt',
            json_config=json.dumps({
                "player": [0, 1],
                "goals": [2, 2],
                "boxes": [1, 2],
                "paths": [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]]
            })
        )
    ]
    db.session.bulk_save_objects(dummy_levels) # Simpely commits the list of objects
    db.session.commit()
    print("Dummy levels populated successfully.")