from datetime import datetime
import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Post(Base):
    __tablename__ = "post"
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

    def decir_titulo(self):
        return "{}".format(self.title)

    def __repr__(self):
        return "{}".format(self.title)


engine = db.create_engine('sqlite:///db.sqlite3')

Base.metadata.create_all(engine)

post = Post(title="Primer post", body="Cuerpo del post")
post.title = "Segundo post"
post.body = "Cuerpo del segundo post"

Session = sessionmaker(bind=engine)

session = Session()

session.add(post)
session.commit()

all_posts = session.query(Post).all()
for post in all_posts:
    print(post.decir_titulo())
