#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: db_create.py
# @Author: eswizardry
# @Date:   2016-09-21 11:47:38
# @Last Modified by:   Bancha Rajainthong
# @Last Modified time: 2016-09-25 13:30:39

from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()

# insert data
db.session.add(Task("Finish this tutorial", date(2016, 9, 30), 10, 1))
db.session.add(Task("Finish Real python", date(2016, 11, 13), 10, 1))

# commit the changes
db.session.commit()
