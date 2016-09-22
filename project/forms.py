# -*- coding: utf-8 -*-
# @Author: Bancha Rajainthong
# @Date:   2016-09-22 21:20:07
# @Last Modified by:   Bancha Rajainthong
# @Last Modified time: 2016-09-22 21:56:42

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, \
    SelectField
from wtforms.validators import DataRequired


class AddTaskForm(Form):
    """docstring for AddTaskFormForm"""
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Date Due (mm/dd/yyyy)',
                         validators=[DataRequired()], format='%m%d%Y')

    priority = SelectField('Priority',
                           validators=[DataRequired()],
                           choices=[('1', '1'), ('2', '2'), ('3', '3'),
                                    ('4', '4'), ('5', '5'), ('6', '6'),
                                    ('7', '7'), ('8', '8'), ('9', '9'),
                                    ('10', '10')])
    status = IntegerField('Status')
