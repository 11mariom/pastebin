# -*- encoding: utf-8 -*-

#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from sqlalchemy import Column, Integer, Text
from database import db
from database import Base

class Paste(Base):
    __tablename__ = 'paste'
    id = Column(Integer, primary_key = True)
    #hash = db.Column(db.String(32), unique = True)
    data = Column(Text())

    def __init__(self):
        return None

    def __repr__(self):
        return '<Paste %r>' % (self.id)  
        #return "<Paste :%s, %s>" % (self.id, self.data)

    def get(self, id):
        return Paste.query.filter_by(id=id).first()

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def put(self, data):
        self.data = data
        db.add(self)
        db.commit()

        return self.id
    
