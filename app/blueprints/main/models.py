from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(300))
    pokes = db.relationship('Pokemon', backref="user", lazy="dynamic")

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)

#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(500))
#    date_created = db.Column(db.DateTime, default = datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#class Post_Comment(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(500))
#    date_created = db.Column(db.DateTime, default = datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#
#    def get_user(self):
#        return User.query.get(self.user_id)
#

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    type = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_user(self):
        return User.query.get(self.user_id)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)