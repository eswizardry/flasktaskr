#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: _config.py
# @Author: eswizardry
# @Date:   2016-09-21 11:42:39
# @Last Modified by:   Bancha Rajainthong
# @Last Modified time: 2016-09-25 15:54:52

import os

# grab the folder where this scripts lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
