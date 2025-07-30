The Sokoban Flask application by Anthony

> Replace the following
sokoban webpage/
├── index.html
├── css/
│   └── style.css
├── images/
│   └── profile.jpg
└── README.md 

How to run from scratch:
1. install python (3.9 though later versions work too) first

2. Install the Flask (the python flask is used to host the server):
pip install flask
or 
pip install -r requirements.txt
(^ If this does not work, you can use 'pip install ___' replaced by the corresponding module)

3. (Optional): if the database.db file needs to be initialised, or is removed for any reason, run the following:
- python setup_db.py
- python populate_levels_with_dummy.py
- python populate_score_with_dummy.py
- python populate_user_with_dummy.py

4. run: python server.py

Make sure that loaded iframes and so new templates have a layout which accomodates for the fact that it is an iframe

> Does not work, no Idea why, use: 'python test_database_existance.py'
To check if the database is created open a new terminal and type:
- sqlite3 database.db
- .tables
- .exit

for testing purposes you may use the following credentials (though you could of course make your own account):
username: 'agha'
password: 'haha'

> Info on how to run/ do tests
Once you are logged into a new account, try to beat a level
If you have completed a level check the leaderboard page to see your new score

P5js can be used to load and test game logic. For it to function you need to take the following folder and paste them under the sketch files head in a new p5js project:
- function.js
- sketch.js
- stylegame.css
- game_engine_test

If nothing seems to be appearing, than that means that json_config is empty in sketch.js
You may grab a config from the populate_levels_with_dummy after the json dump part, and paste it into the json_config within the sketch.hs file