"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    #Setting up data model for model table
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50))
    name = db.Column(db.String(50), nullable=False)

    brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        return "<Model id=%s, year=%s, brand_name=%s, name=%s>" % (self.id,
                                                                self.year,
                                                                self.brand_name,
                                                                self.name)


class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    #Setting up data model for brand table
    id = db.Column(db.Integer,
                   db.ForeignKey('models.id'),
                   primary_key=True,
                   autoincrement=True,
                   )
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        return "<Brand id=%s, brand_name=%s, discontinued=%s, founded=%s>" % (self.id,
                                                                              self.name,
                                                                              self.discontinued,
                                                                              self.founded)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
