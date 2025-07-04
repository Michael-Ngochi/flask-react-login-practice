from . import db 
from sqlalchemy import Column, Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__="users"

    id =db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    email=db.Column(db.String(120), unique=True)
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash=db.Column(db.String(128))


    role = relationship('Role', backref='users')


    def setpassword(self, password):
        self.password_hash=generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.password_hash,password)