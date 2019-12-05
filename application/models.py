from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

#remember to set a foreign key - potentially done

class shen_user(db.Model,UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    pasword = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.user_id), '\r\n'
            'Username: ', self.username, '\r\n'
            'Email: ', self.email, '\r\n'
        ])


class shen_gong(db.Model):
    shen_id = db.Column(db.Integer, primary_key=True)
    shen_name = db.Column(db.String(30), nullable=False)
    power_rating = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return ''.join([
            'Shen Name: ', self.shen_name, '\r\n'
            'Power Rating: ', self.power_rating, '\r\n'
            'Description: ', self.description, '\r\n'
        ])

@login_manager.user_loader
def load_user(id):
    return shen_user.query.get(int(id))
