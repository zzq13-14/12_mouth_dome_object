from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key='qwertyuiop'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:258000@localhost/music_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)

class Music(db.Model):
    __tablename__='music_1'
    music_id=db.Column(db.INT,primary_key=True,autoincrement=True)
    music_title=db.Column(db.String(1500),unique=False,nullable=False)
    music_url=db.Column(db.String(1500),unique=False,nullable=False)


    def __init__(self,music_title,music_url):
        # self.music_id=music_id
        self.music_title=music_title
        self.music_url=music_url


    def __repr__(self):
        return '%s'%self.music_id


# db.create_all()