from server import db, app, User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)  # Initialize Bcrypt with your app

with app.app_context():
    hashed_password = bcrypt.generate_password_hash('haha').decode('utf-8')
    dummy_user = User(username='agha', password=hashed_password)
    db.session.add(dummy_user)
    db.session.commit()

    hashed_admin_password = bcrypt.generate_password_hash('thecakemightbelyingngl').decode('utf-8')
    dummy_admin_user = User(username='adminagha', password=hashed_admin_password, is_admin=True)

    db.session.add(dummy_admin_user)
    db.session.commit()

    print("Dummy users created successfully with passwords.")