#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb,sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Mysql():

    @staticmethod
    def connet():
        #连接数据库
        conn=MySQLdb.connect(host='192.168.30.28',port=3306,user='root',passwd='admin',db='testjzs',charset="utf8")
        handle=conn.cursor()
        return handle,conn

    @staticmethod
    def select_testerwork(handle,name):
        strsql="select mobile,worktime,txtime,avgtime,csxl from info where Name='%s'"%name
        handle.execute(strsql)
        tup=handle.fetchall()
        # print tup
        return  tup
    @staticmethod
    def insert_testerwork(handle,worktimels,avgtimels,txtimels,csxlls,mobilels):

        for index in range(len(worktimels)):
            strsql_2="update info set worktime='%s',avgtime='%s',txtime='%s',csxl='%s' where mobile='%s'"%\
                     (worktimels[index],avgtimels[index],txtimels[index],csxlls[index],mobilels[index])
            handle.execute(strsql_2)

    @staticmethod
    def select_Name(handle):
        strsql="select Name from info "
        handle.execute(strsql)
        tup=handle.fetchall()
        # print tup
        return  tup





    @classmethod
    def close(cls,handle,conn):
        handle.close()
        conn.close()
