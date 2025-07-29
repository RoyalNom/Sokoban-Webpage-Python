from server import db, app, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)  # Initialize Bcrypt with your app

with app.app_context():
    hashed_password = bcrypt.generate_password_hash('haha').decode('utf-8')

    dummy_user = User(username='agha', password=hashed_password)

    db.session.add(dummy_user)
    db.session.commit()

    print("Dummy user created successfully with bcrypt-hashed password.")