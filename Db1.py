import psycopg2
import psycopg2.extras
from datetime import datetime, date
from psycopg2._psycopg import DatabaseError
import sys
import ConfigParser
import csv

""" For using when a config file is used to set database parameter"""
# config = ConfigParser.RawConfigParser()
# config.read('pyconfig.conf')
# dbconfig_parm = dict(config.items('postgresql'))
# conn = None


f = open('New.csv', 'rb') # CSV file name
record_csv = csv.reader(f, delimiter='|')

new_data = []
header = record_csv.next()

for row in record_csv:
    new_data.append(dict(zip(header, row)))
f.close()

try:
    conn = psycopg2.connect(host="localhost", database="AssignmentDB", user="postgres", password="kamareee34") # connecting to postgres DB
    # conn = psycopg2.connect(**dbconfig_parm)
    conn.set_session(autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    for i in new_data:
        insert_qry = "INSERT INTO Website (date, website, visits) VALUES (%s, %s, %s)"
        cur.execute(insert_qry, (i['date'], i['website'], i['visits']))
        print "Query executed successfully"


except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit(1)

finally:
    if conn is not None:
        conn.close()