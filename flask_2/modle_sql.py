from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key='qwertyuiop1'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:******@localhost/music_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)


#DJ 音乐网模型
class Music(db.Model):
    __tablename__='music_2'
    music_id=db.Column(db.INT,primary_key=True,autoincrement=True)
    music_title=db.Column(db.String(1500),unique=False,nullable=False)
    music_url=db.Column(db.String(1500),unique=False,nullable=False)
    music_url_audio=db.Column(db.String(1500),unique=False,nullable=False)


    def __init__(self,music_title,music_url,music_url_audio):
        # self.music_id=music_id
        self.music_title=music_title
        self.music_url=music_url
        self.music_url_audio=music_url_audio


    def __repr__(self):
        return '%s'%self.music_id


Hao_123 网址模型
class Music_Player(db.Model):
    __tablename__='music_player'
    player_id=db.Column(db.INT,primary_key=True,autoincrement=True)
    player_title=db.Column(db.String(500),nullable=False)
    player_url=db.Column(db.String(500),nullable=False)

    def __init__(self,player_title,player_url):
        self.player_title=player_title
        self.player_url=player_url


# db.create_all()
