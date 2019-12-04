# -*- coding: utf-8 -*-
"""demo_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JrXMaTS2mRaaWBbZMJosXtrPd5jVCTg1
"""

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

conn

curs = conn.cursor()

demo_data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

curs.execute('CREATE TABLE demo (s char(20), x int, y int);')

for dat in demo_data:
  insert_query = curs.execute('INSERT INTO demo (s, x, y) VALUES ' + str (dat))

insert_query

curs.close()

conn.commit()

curs = conn.cursor()

curs.execute('SELECT COUNT(*) FROM demo;').fetchall()

curs.execute('SELECT COUNT(*) FROM demo WHERE x>5 AND y>5;').fetchall()

curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall()

