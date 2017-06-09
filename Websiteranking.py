import psycopg2
import psycopg2.extras
from datetime import datetime, date
from psycopg2._psycopg import DatabaseError
import sys
#import ConfigParser

""" For using when a config file is used to set database parameter"""
# config = ConfigParser.RawConfigParser()
# config.read('pyconfig.conf')
# dbconfig_parm = dict(config.items('postgresql'))
# conn = None

try:
    conn = psycopg2.connect(host="localhost", database="AssignmentDB", user="postgres", password="kamareee34") # connecting to postgres DB
    # conn = psycopg2.connect(**dbconfig_parm)
    conn.set_session(autocommit=True)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    qry1 = "SELECT * FROM website WHERE date='2013-01-06'"
    cur.execute(qry1)
    result = cur.fetchall()
    
    if result is None:
        print("There is no such date in the database")
    else:
        qry_final = "SELECT * FROM website WHERE date='2013-01-06' ORDER BY visits DESC LIMIT 5"
        cur.execute(qry_final)
        res_final = cur.fetchall()
        for i in res_final:
            print("Website: ", i['website'] + '  |  ' + "Visitors: ", i['visits'])


except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    sys.exit(1)

finally:
    if conn is not None:
        conn.close()