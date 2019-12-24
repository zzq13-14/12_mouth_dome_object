from flask import Flask,render_template
from music_sql import *
app = Flask(__name__)

app.secret_key='qwertyuiop1'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:258000@localhost/music_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)

# @app.route('/')
# def hello_world():
    # return 'Hello World!'
@app.route('/',methods=['GET','POST'])
def hello_world():
    # info=
    res=Music.query.all()
    return render_template('show.html',res=res)


if __name__ == '__main__':
    app.run(debug=True)
