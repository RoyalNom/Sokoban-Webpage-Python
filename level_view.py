# run with: python level_view.py
# take it out of the test folder to run it
from server import app, db, Levels

with app.app_context():
    levels = Levels.query.all()
    for level in levels:
        print(f"Level ID: {level.level_id}, Author: {level.author}, JSON: {level.json_config[:60]}...")