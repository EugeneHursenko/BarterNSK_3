from app import db
from flask_login import UserMixin

ROLE_USER = 0
ROLE_ADMIN = 1


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)
    password = db.Column(db.String(100))
    is_enabled = db.Column(db.Boolean(), default=0, index=True)

    def __repr__(self):
        return '<User %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % self.title


class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Offer %r>' % self.title


# class Test2(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), index=True)
#     description = db.Column(db.Text)
#
#     def __repr__(self):
#         return '<Test2 %r>' % self.title
