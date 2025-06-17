from . import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Role(db.Model):
    __tablename__='roles'

    id =db.Column(Integer, primary_key = True)
    role_name=db.Column(String, nullable=False)