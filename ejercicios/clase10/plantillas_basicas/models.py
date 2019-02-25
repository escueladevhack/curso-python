"""
This code was taked form [flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/)
"""

from datetime import datetime

from database import db

class Post(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String(80),
        nullable=False
    )
    body = db.Column(
        db.Text,
        nullable=False
    )
    pub_date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __str__(self):
        return "{}".format(self.title)

