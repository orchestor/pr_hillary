from pr_hillary.extensions import db
from pr_hillary.models.relationships import tags_posts
from pr_hillary.database import (
    Model,
    SurrogatePK,
)


class Tag(SurrogatePK, Model):

    __tablename__ = 'tags'

    tag = db.Column(db.Text)
    posts = db.relationship('Post', secondary=tags_posts, backref=db.backref('tags_br', lazy='dynamic'))

    def __init__(self, tag, **kwargs):
        db.Model.__init__(self, tag=tag, **kwargs)