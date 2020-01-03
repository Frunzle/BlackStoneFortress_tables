import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template ("index.html")

@app.route("/behaviour")
def behaviour():
    return render_template("enemybehaviour.html")

@app.route("/inputbehaviour", methods= ["GET", "POST"])
def inputbehaviour():
    actions = db.execute("SELECT * FROM hostileactions").fetchall()

    if request.method=="POST":
        actionname = request.form.get("actionname")
        description = request.form.get("description")
        print (f"{actionname}, {description}")
        db.execute("INSERT INTO hostileactions (actionname, description) VALUES (:actionname, :description)",
                     {"actionname": actionname, "description": description})
        db.commit()
    return render_template("behaviourinput.html", actions = actions)
    
@app.route("/inputhostiles", methods=["GET" , "POST"])
def inputhostiles():
    hostiles = db.execute("SELECT * FROM hostiles").fetchall()

    if request.method=="POST":
        hostilename = request.form.get("hostilename")
        hostilemove = request.form.get("hostilemove")
        hostilewounds = request.form.get("hostilewounds")
        hostilesize = request.form.get("hostilesize")
        db.execute("INSERT INTO hostiles (hostilename, hostilemove, hostilewounds, hostilesize) VALUES (:hostilename, :hostilemove, :hostilewounds, :hostilesize)", {"hostilename":hostilename, "hostilemove":hostilemove, "hostilewounds":hostilewounds, "hostilesize":hostilesize})
        db.commit()
    return render_template("hostileinput.html", hostiles = hostiles)
