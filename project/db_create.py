#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: db_create.py
# @Author: eswizardry
# @Date:   2016-09-21 11:47:38
# @Last Modified by:   eswizardry
# @Last Modified time: 2016-09-21 15:58:58

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    due_date TEXT NOT NULL,
                                    priority INTEGER NOT NULL,
                                    status INTERGER NOT NULL)
              """)

    # insert dummy data into the table
    c.execute('INSERT INTO tasks(name, due_date, priority, status)'
              'VALUES("Finish this tutorial", "09/23/2016", 10, 1)'
              )

    c.execute('INSERT INTO tasks(name, due_date, priority, status)'
              'VALUES("Finish Real Python Course 2", "10/31/2016", 10, 1)'
              )