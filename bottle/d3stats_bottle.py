#!/usr/bin/python

from bottle import route, run, template
import MySQLdb

@route('/hello')
def hello():
	return 'Hello World!'

@route('/insert_run/<total_time>/<map_id>/<xp_gain>/<legend_drops>/<goblin_count>/<gold_gain>/<y_mobs>/<b_mobs>/<p_mobs>/<difficulty>/<notes>')
def insert_run(total_time,map_id,xp_gain,legend_drops,goblin_count,gold_gain,y_mobs,b_mobs,p_mobs,difficulty,notes):
	try:
		# establish connections
		conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="d3stats_staging")
		cur = conn.cursor()
		# build insert statement 
		cur.execute("""INSERT INTO run (total_time,map_id,xp_gain,legend_drops,goblin_count,gold_gain,y_mobs,b_mobs,p_mobs,difficulty,notes) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",('2014-04-04 00:30:00',map_id,xp_gain,legend_drops,goblin_count,gold_gain,y_mobs,b_mobs,p_mobs,difficulty,notes))
		conn.commit()
		return 'woot success!'
	except MySQLdb.Error, e:
		return "there was an error"

run(host='107.170.195.104', port=8080, debug=True)
