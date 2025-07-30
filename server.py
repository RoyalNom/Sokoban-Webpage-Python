import os
import json
from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from database_logic import update_score

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
"""
class Score(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    moves = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Score('{self.username}', '{self.score}')"
"""
class ScoreMoves(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    moves = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Float, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('username', 'level', name='unique_username_level'),
    )

class ScoreTime(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    moves = db.Column(db.Integer, nullable=False)
    time_taken = db.Column(db.Float, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('username', 'level', name='unique_username_level'),
    )

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

# Leaderboard routes logic, with a default route to moves level 1
@app.route('/leaderboard') 
def default_leaderboard():
    return redirect(url_for('leaderboard_moves', level='1'))

@app.route('/leaderboard/moves/<level>')
def leaderboard_moves(level):
    scores = ScoreMoves.query.filter_by(level=level).order_by(ScoreMoves.moves.asc()).all()
    return render_template('leaderboard.html', scores=scores, selected_level=level, mode='moves')

@app.route('/leaderboard/time/<level>')
def leaderboard_time(level):
    scores = ScoreTime.query.filter_by(level=level).order_by(ScoreTime.time_taken.asc()).all()
    return render_template('leaderboard.html', scores=scores, selected_level=level, mode='time')

@app.route('/game_engine/<level_id>')
@login_required
def game_engine_with_level(level_id):
    level = Levels.query.filter_by(level_id=level_id).first()
    if level:
        config = json.loads(level.json_config)
        return render_template('game_engine.html', config=config, selected_level=level_id)
    else:
        return f"No such level: {level_id}", 404
    
@app.route('/update_score', methods=['POST'])
def update_score():
    try:
        data = request.get_json()
        username = data['username']
        level = data['level']
        moves = int(data['moves'])
        time_taken = float(data['time_taken'])

        print(f"[DEBUG] Received: {username}, Level: {level}, Moves: {moves}, Time: {time_taken}")

        # Your existing DB logic here...
        existing_move = ScoreMoves.query.filter_by(username=username, level=level).first()
        if existing_move:
            existing_move.moves = min(existing_move.moves, moves)
            existing_move.time_taken = time_taken
        else:
            db.session.add(ScoreMoves(username=username, level=level, moves=moves, time_taken=time_taken))

        existing_time = ScoreTime.query.filter_by(username=username, level=level).first()
        if existing_time:
            existing_time.time_taken = min(existing_time.time_taken, time_taken)
            existing_time.moves = moves
        else:
            db.session.add(ScoreTime(username=username, level=level, moves=moves, time_taken=time_taken))

        db.session.commit()
        return jsonify({'status': 'success'})

    except Exception as e:
        print("[ERROR] Score update failed:", e)  # Logs error to your terminal
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)