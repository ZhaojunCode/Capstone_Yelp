#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('yelpinstance.cxef9crs1tzb.us-east-1.rds.amazonaws.com', #localhost
	'yelperuser', # user
	'yelpee321', # pw
	'yelper_prod'); # db

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM clean_businesses LIMIT 50")

    # fetch rows
    rows = cur.fetchall()
    
    # store column names
    desc = cur.description

    print "%s %s %s  %s %s  %s %s  %s %s  %s %s %3s" % (desc[0][0], 
    	desc[1][0], desc[2][0], desc[3][0], desc[4][0], desc[5][0],
    	desc[6][0], desc[7][0], desc[8][0], desc[9][0], desc[10][0],
    	desc[11][0])

    for row in rows:
        print row

# 1. Read in data (business_id's?) from model prediction
# 2. Fix the output so they aren't tuples.
# 3. Improve the god awful lines 23-26.