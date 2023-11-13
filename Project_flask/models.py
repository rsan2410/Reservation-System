from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Booking(db.Model):
  id = db.Column(db.String(12), primary_key=True)
  partySize = db.Column(db.Integer)
  time = db.Column(db.String(5))
  specReq = db.Column(db.String(350))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  date_id = db.Column(db.Integer, db.ForeignKey('bookDate.id'))

class BookDate(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Integer)
  day = db.Column(db.String(9))
  month = db.Column(db.String(9))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  firstName = db.Column(db.String(15))
  surname = db.Column(db.String(15))
  password = db.Column(db.String(15))
  bookings = db.relationship('Booking')