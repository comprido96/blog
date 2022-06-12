"""Data Models"""
from . import db


class Post(db.Model):
	__tablename__ = 'posts'
	
	id = db.Column(
        db.Integer,
        primary_key=True
	)

    author = db.Column(
        db.String(64),
        index = True,
        nullable = False
    )

    title = db.Column(
        db.String(64),
        index = True,
        nullable = False
    )

    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    
    body = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )

    admin = db.Column(
        db.Boolean,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return f'<Author: {self.author} - title: {self.title} - created on: {self.created}>'