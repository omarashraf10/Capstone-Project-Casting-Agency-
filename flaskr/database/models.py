
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

database_path = os.getenv('DATABASE_URL')
db = SQLAlchemy()


def setupDB(app,database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    #app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Email1087@localhost:5432/agency'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    
    

def createAll():
    db.create_all()

def setupMigration(app):
    migrate = Migrate(app, db)
    
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)
    genre = db.Column(db.String(), nullable=False, default='')


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return({
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date.isoformat(),
            "genre": self.genre
        })

    def __repr__(self):
        return f'Movie:{self.id}, {self.title}'




class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return({
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        })

    def __repr__(self):
        return f'Actor: {self.id}, {self.name}'


