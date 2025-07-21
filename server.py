import os
import json
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# db = SQLAlchemy(app) # Initialize Database
bcrypt = Bcrypt(app)  # Initialize Bcrypt for password hashing

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SECRET_KEY'] = 'whatsecretkey' # Secret key for session management, MUST BE CHANGED FOR DEPLOYMENT

db = SQLAlchemy(app) # Initialize Database

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Table for login information
class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_id(self):
        return str(self.user_id)

# Table for leaderboard scores information
class Score(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    moves = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Score('{self.username}', '{self.score}')"

class Levels(db.Model):
    level_id = db.Column(db.String(30), primary_key=True) # 1 to 4 for the base levels, normal names for custom levels
    author = db.Column(db.String(20), nullable=False)
    json_config = db.Column(db.Text, nullable=False)


# Registration form, (there might be a better way to do this)
class RegistrationForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=username.data).first()

        # Check if the username already exists in the database
        # A different way to commincate this is error should be developed
        if existing_user:
            raise ValidationError('Username already exists. Please choose a different one.')
            

# Login form
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # Checks if user exists
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            # return redirect(url_for('dashboard'))
            return '''
                <script type="text/javascript">
                    window.top.location.href = "/";
                </script>
            '''
        else:
            return "Login Unsuccessful. Please check username and password."
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/leaderboard') # Default leaderboard route
def leaderboard_all():
    scores = Score.query.all()
    return render_template('leaderboard.html', scores=scores)

@app.route('/leaderboard/<level>/<sort_by>') # Creates routes (subsets of Score table) based on query filtrering for both the amount of moves and time taken
def leaderboard_by_level_sorted(level, sort_by):
    if sort_by == 'moves':
        scores = Score.query.filter_by(level=level).order_by(Score.moves.asc()).all()
    elif sort_by == 'time':
        scores = Score.query.filter_by(level=level).order_by(Score.time_taken.asc()).all()
    else:
        scores = Score.query.filter_by(level=level).all()
    return render_template('leaderboard.html', scores=scores, selected_level=level, sort_by=sort_by) # Pass the selected level and sort_by to the template

@app.route('/play/<level_id>')
@login_required
def play_level(level_id):
    level = Levels.query.filter_by(level_id=level_id).first()
    if level:
        config = json.loads(level.json_config)
        return render_template('thegame.html', config=config)
    else:
        return f"No such level: {level_id}", 404

if __name__ == '__main__':
    app.run(debug=True)