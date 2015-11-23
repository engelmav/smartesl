from settings import DB_CXN_STR
import psycopg2, json
import sql_lib as sql

class DBAccessor(object):

    def __init__(self):
        print "Creating connection to " + DB_CXN_STR
        self.conn = psycopg2.connect(DB_CXN_STR)
        self.cur = self.conn.cursor()