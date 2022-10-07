#!/usr/bin/python3
import unittest
import requests
import json
import sqlite3

class TestDB(unittest.TestCase):
	def test_age_18_50(self):
        	conn=sqlite3.connect('database.db')
        	cur=conn.cursor()
        	cur.execute('select age from utilisateurs where age<18 or age>50')
        	self.assertEqual(len(cur.fetchall()), 0, msg="Il y a des âges sup à 50 ou inf à 18 !!!")
        	cur.close()

   	def test_pas_communes_francaise(self):
		cmn_fr=[]
		conn=sqlite3.connect('database.db')
		  cur=conn.cursor()
		cur.execute('select distinct ville from utilisateurs')
		  rows=cur.fetchall()
		r= requests.get("https://geo.api.gouv.fr/communes?codeDepartement=15")
		j=r.json()
		for i in range(len(j)):
			cmn_fr.append(j[i]["nom"])
		for v in range(len(rows)):
			self.assertNotIn(rows[v], cmn_fr, msg="La commune {} est une ville francaise!!!".format(rows[v]))
