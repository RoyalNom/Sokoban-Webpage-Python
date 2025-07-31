# run with: python delete_level.py
from server import app, db, Levels

with app.app_context():
    level_name = "gridtest1"  # Replace with the name of the level
    level = Levels.query.filter_by(level_id=level_name).first()
    if level:
        db.session.delete(level)
        db.session.commit()
        print(f"Level '{level_name}' deleted.")
    else:
        print(f"No level found with name '{level_name}'.")