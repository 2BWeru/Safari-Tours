from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
       return User.query.get(int(user_id))


class User(db.Model,UserMixin):
  __tablename__= 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),unique = True)
  email = db.Column(db.String(255),unique = True,index = True)
  password_hash = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  profile_pic_path = db.Column(db.String())
  comment = db.relationship('Comment',backref='user',lazy='dynamic')
  booking = db.relationship('Booking',backref='user',lazy='dynamic')
   
  def save_user(self):
      db.session.add(self)
      db.session.commit()
  def delete(self):
      db.session.delete(self)
      db.session.commit()

  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)

  def __repr__(self):
        return f'User {self.username}'


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255),unique = True)
    email = db.Column(db.String(255),nullable = False)
    phone = db.Column(db.String(255),nullable = False)
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
     
    def save_b(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_bookings(cls,id):
        booking = Booking.query.filter_by(user_id=id).all()
        return booking

        
    def __repr__(self):
        return f'Booking {self.email}'

# comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255),unique = True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    
