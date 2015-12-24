#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  db tool
import pymysql
import os
import sys
import os
import json
from seting import applog
import time

class mysql:
    """ Class doc """

    def __init__ (self,curtype):
        """ Class initialiser """
        fname = os.path.join(os.path.dirname(__file__), "./config/databases.json")
        if os.path.exists(fname):
            f = open(fname)
            self.databases = json.load(f)
            f.close()
        self.connections = []
        for params in self.databases:
            self.connections.append(pymysql.connect(**params))
        #self.connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='easydb',charset="utf8")
        if curtype == "dict" :
            self.curtype = pymysql.cursors.DictCursor
        else:
            self.curtype = None


    def tearDown(self):
        for connection in self.connections:
            connection.close()

    def getAlldict(self,query_sql):
        applog.debug("sql: %s" ,query_sql)
        conn = self.connections[0]
        cur = conn.cursor(self.curtype)
        cur.execute(query_sql)
        rows = cur.fetchall()
        return rows

    def exemany(self,query_sql,args):
        conn =  self.connections[0]
        cur = conn.cursor()
        re = cur.executemany(query_sql,args)
        return re

    def exesql(self,query_sql):
        conn =  self.connections[0]
        cur = conn.cursor()
        applog.debug(query_sql)
        re = cur.execute(query_sql)
        return re

    def exedelete(self,query_sql):
        conn =  self.connections[0]
        cur = conn.cursor()
        cur.execute(query_sql)
        return 1

    def getOnedict(self,query_sql):
        conn = self.connections[0]
        cur = conn.cursor(self.curtype)
        cur.execute(query_sql)
        row = cur.fetchone()
        applog.debug (row)
        return row
    def commit(self):
        cnn = self.connections[0]
        cnn.commit()

    def backUpDateBase(self): 
        approot=''
        try:
            approot = os.path.dirname(os.path.abspath(__file__))
        except NameError: 
            approot = os.path.dirname(os.path.abspath(sys.argv[0]))
    
        for params in self.databases:            
            today = time.strftime('%Y-%m-%d')
            backfilename='%s/%s_%s.sql'   %(os.path.join(approot, 'database'),params.get('db'),today)
            applog.debug("save database file : %s" %(backfilename))
            bak_shell="C:/mysql-5.6.23-win32/bin/mysqldump -u %s -p%s -R %s > %s " %(params.get('user'),params.get('passwd'),params.get('db'),backfilename)
            applog.debug(bak_shell)
            os.system(bak_shell)
        applog.info("backup database end !!")
        return True    



def test_example():
    #conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='easydb',charset="utf8")

    query_sql=" select * from   meum_sidebar"
    ms = mysql(curtype="dict")
    ms.backUpDateBase()

    #conn.close()

def test():
    test_example()

if __name__ == "__main__":
    test()
