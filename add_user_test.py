from server import db, User, app

with app.app_context():
    test_user = User(username='testuser', password='testpass123')
    db.session.add(test_user)
    db.session.commit()
    print("Test user added successfully.")

# Then run 'select * from user;' in sqlite3 logindatabase.db' for verfication
# Comment: The password is not hashed