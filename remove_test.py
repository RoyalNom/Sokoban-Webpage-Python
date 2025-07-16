from server import db, User, app

with app.app_context():
    user_to_delete = User.query.filter_by(username='testuser').first()

    if user_to_delete:
        db.session.delete(user_to_delete)
        db.session.commit()
        print("Test user removed successfully.")
    else:
        print("User 'testuser' not found.")