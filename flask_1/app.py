from flask import Flask,request,render_template,flash,redirect,url_for
from music_sql import *

app = Flask(__name__)

app.secret_key='qwertyuiop'

app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:258000@localhost/music_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db=SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def hello_world():
    res=Music.query.all()
    return render_template('show.html',res=res)


if __name__ == '__main__':
    app.run(debug=True)
