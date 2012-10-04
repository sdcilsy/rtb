# -*- coding: utf-8 -*-
'''
Created on Mar 12, 2012

@author: moloch

    Copyright 2012 Root the Box

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


import json


from uuid import uuid4
from sqlalchemy import Column
from sqlalchemy.types import Unicode, Integer
from models.BaseGameObject import BaseObject
from models import dbsession


class MarketItem(BaseObject):
    ''' Item definition '''

    uuid = Column(Unicode(36), unique=True, nullable=False, default=lambda: unicode(uuid4()))
    name = Column(Unicode(64), nullable=False)
    price = Column(Integer, nullable=False)
    image = Column(Unicode(255))
    description = Column(Unicode(1024))
    permission_name = Column(Unicode(64), nullable=False)

    @classmethod
    def all(cls):
        ''' Returns a list of all objects in the database '''
        return dbsession.query(cls).all()

    @classmethod
    def by_id(cls, ident):
        ''' Returns a the object with id of ident '''
        return dbsession.query(cls).filter_by(id=ident).first()

    @classmethod
    def by_uuid(cls, uuid):
        ''' Returns a the object with a given uuid '''
        return dbsession.query(cls).filter_by(uuid=unicode(uuid)).first()

    @classmethod
    def by_name(cls, name):
        ''' Returns an object with a given name '''
        return dbsession.query(cls).filter_by(name=unicode(name)).first()

    def to_json(self):
        ''' Returns object data as json object '''
        msg = {
            'name': self.name,
            'price': self.price,
            'image': self.image,
            'description': self.description,
            'uuid': self.uuid,
        }
        return msg