from server import db, User, app

with app.app_context():
    test_user = User(username='testuser', password='testpass123')
    db.session.add(test_user)
    db.session.commit()
    print("Test user added successfully.")