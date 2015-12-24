#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  dbtool import mysql
from seting import config,applog
import time

class userinfo:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)

        self.type =type
        self.username = ''.join(dict.get('record[username]'))
        self.password =''.join(dict.get('record[password]'))
        self.records = []
        
    
    def login(self):
        query_sql= 'SELECT recid,password FROM  userinfo where username=%r' %(self.username)
        applog.debug(query_sql)
        ms = mysql(curtype=None)
        re = ms.getAlldict(query_sql)
        applog.debug(re)
        if len(re)<1 or re is None :
            return False    
        
        for uid,passwd in re:
            applog.debug(uid,passwd)
            if passwd == self.password :
                self.recid = uid
                break
            else:
                return False
        return True

class sidebarnodes:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)

        self.type =type
        self.sidebar_id = dict.get('record[recid]')
        self.sidebar_code =dict.get('record[sidebar_code]')
        self.sidebar_text = dict.get('record[sidebar_text]')
        self.sidebar_img = dict.get('record[sidebar_img][id]')
        self.expanded = dict.get('record[expanded][id]')
        self.prant_code = dict.get('record[prant_code][id]')
        self.web_template = dict.get('record[web_template]')
        self.tablename = dict.get('record[tablename]')
        self.sort_number = dict.get('record[sort_number]')
        self.sidebarstate = dict.get('record[sidebarstate][id]')
        self.records = []

    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.sidebar_code[length],self.sidebar_text[length],self.sidebar_img[length],self.expanded[length],self.prant_code[length],self.web_template[length],self.tablename[length],self.sort_number[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.sidebar_code[length],self.sidebar_text[length],self.sidebar_img[length],self.expanded[length],self.prant_code[length],self.web_template[length],self.tablename[length],self.sort_number[length],self.sidebarstate[length],self.sidebar_id[length]))
                else:
                    pass
            applog.debug(self.records)
        return self.records

    def getSidebarAll(self):
        query_sql= config['getSidebar']['prantsiderbr']
        ms = mysql(curtype="dict")
        re = ms.getAlldict(query_sql)

        dict2 ={'group': 'true'}
        nodes =[]
        dictMerged2={}
        for dict1  in re:
            dictMerged2=dict(dict1, **dict2)
            ch_sql=config['getSidebar']['chrildsiderbr'] %(dict1.get('id'))
            applog.debug(ch_sql)
            getre = ms.getAlldict(ch_sql)
            if (len(getre)>0):
                dictMerged2['nodes']=getre
            nodes.append(dictMerged2)
        ms.tearDown()
        return nodes


class panleTabsTabs:

    def __init__(self,tabid,name):
        self.scode=tabid
        self.records=None
        self.table =name
        self.total = 0


    def showTabsTemplate(self):
        query_sql= config['getSidebar']['tabsTemplate']  %(self.scode)
        applog.debug(query_sql)
        ms = mysql(curtype="")
        tplnames = ms.getOnedict(query_sql)
        self.table =tplnames[1]
        ms.tearDown()
        return tplnames

    def desc_reprot(self):
        query_sql= config['reprotDesc']['columns']
        applog.debug(query_sql)
        ms = mysql(curtype="dict")
        re = ms.getAlldict(query_sql)
        return re

class prouductList:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)

        self.type =type
        self.product_id = dict.get('record[recid]')
        self.class_id =dict.get('record[class_id][id]')
        self.product_name = dict.get('record[product_name]')
        self.product_code = dict.get('record[product_code]')
        self.unit_price = dict.get('record[unit_price]')
        self.unit_type = dict.get('record[unit_type]')
        self.remark = dict.get('record[remark]')
        self.records = []

    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.class_id[length],self.product_name[length],self.product_code[length],self.unit_price[length],self.unit_type[length],self.remark[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.class_id[length],self.product_name[length],self.product_code[length],self.unit_price[length],self.unit_type[length],self.remark[length],self.product_id[length]))
                else:
                    pass
        return self.records


class prouductClass:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)
        self.type =type
        self.class_id = dict.get('record[recid]')
        self.class_code =dict.get('record[class_code]')
        self.class_name = dict.get('record[class_name]')
        self.remark = dict.get('record[remark]')
        self.records = []

    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.class_code[length],self.class_name[length],self.remark[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.class_code[length],self.class_name[length],self.remark[length],self.class_id[length]))
                else:
                    pass
            applog.debug(self.records)
        return self.records



class comsumeDetail:
    def __init__(self,type,dict):
        applog.debug(dict)
        self.recid = dict.get('recid')
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)
        self.type =type      
        
        self.detail_list_id =dict.get('record[recid]')
        self.consume_date =dict.get('record[consume_date]')
        self.fee = dict.get('record[fee]')
        self.amount = dict.get('record[amount]')
        self.product_id = dict.get('record[product_id][id]')
        self.insert_time = dict.get('record[insert_time]')
        self.remark = dict.get('record[remark]')
        if (self.detail_list_id is None):
            self.detail_list_id =['']            
        if (self.consume_date is None):
            self.consume_date =['']
        if (self.fee is None):
            self.fee =[0]
        if (self.amount is None):
            self.amount =[0]
        if (self.product_id is None):
            self.product_id = ['']
        if (self.insert_time is None):
            self.insert_time = ['']
        if (self.remark is None):
            self.remark = ['']
        
        self.records = []

    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.consume_date[length],self.fee[length],self.product_id[length],self.insert_time[length],self.remark[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.consume_date[length],self.fee[length],self.product_id[length],self.insert_time[length],self.remark[length],self.detail_list_id[length]))
                else:
                    pass
            applog.debug(self.records)
        return self.records


class comsumeList:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)
        self.type =type
        self.consume_list_id = dict.get("record[recid]")
        self.consume_date =dict.get('record[consume_date]')
        self.class_id = dict.get('record[class_id][id]')
        self.sum_fee = dict.get('record[sum_fee]')
        self.consume_state = dict.get('record[consume_state][id]')
        self.insert_time = dict.get('record[insert_time]')
        self.remark = dict.get('record[remark]')
        self.records = []


    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.consume_date[length],self.class_id[length],self.sum_fee[length],self.consume_state[length],self.insert_time[length],self.remark[length]))
                elif(self.type == 'edit'):
                        self.records.append((self.consume_date[length],self.class_id[length],self.sum_fee[length],self.consume_state[length],self.insert_time[length],self.remark[length],self.consume_list_id[length]))
                else:
                    pass
            applog.debug(self.records)
        return self.records

class report_info:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)
        self.type =type
        self.report_id = dict.get("record[recid]")
        self.consume_date =dict.get('record[consume_date][id]')
        self.report_state = dict.get('record[report_state][id]')
        self.report_year = dict.get('record[report_year][id]')
        self.records = []


    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.report_year[length],self.report_state[length],getPmonth(self.consume_date[length]),self.consume_date[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.consume_date[length],self.report_state[length],self.report_year[length],self.report_id[length]))
                else:
                    pass
            applog.debug(self.records)
        return self.records

    

class year_report:
    def __init__(self,type,dict):
        self.length =0
        self.dict=dict
        self.recid=None
        if dict is not None:
            self.recid = dict.get('recid')
            if(self.recid is None):
                self.length =0
            else:
                self.length = len(self.recid)
            self.type =type
            self.report_id = dict.get("record[recid]")
            self.consume_date =dict.get('record[consume_date]')
        self.records = []
        
        self.wheresql=''
        
    def getseacher(self):
        print('ttt:%s' %(self.dict) )
        dict=self.dict
        
        sl = dict.get('searchLogic')
        if (sl is not None):
            self.searchlogic = ''.join(sl)
            applog.debug(self.searchlogic)
        wheresql1 = ''
        
        for idx in range(len(dict)) :
            applog.debug(idx)
            ssearchfield_key = 'search[%s][field]' %(idx)
            searchvalue_key = 'search[%s][value]'  %(idx)
            opera_key = 'search[%s][operator]'  %(idx)
            if(dict.get(ssearchfield_key) is None):
                break
            else:
                ssearchfield = ''.join(dict.get(ssearchfield_key))
                searchvalue = ''.join(dict.get(searchvalue_key ))
                opera = ''.join(dict.get( opera_key))
                wheresql0 =''
                if (opera == 'is'):
                    operator ='='
                    wheresql0 = " %s  aa.%s = %r " %(self.searchlogic,ssearchfield,searchvalue)
                elif (opera == 'ends'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,'%'+searchvalue)
                elif (opera == 'begins'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,searchvalue+'%')
                elif (opera == 'contains'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,'%'+searchvalue+'%')
                else:
                    pass
            wheresql1 = wheresql1 + wheresql0
            applog.debug(wheresql0)
        self.wheresql = wheresql1
        applog.debug('seacher sql :%s'  %(self.wheresql))

    def getparam(self):
        return self.records
    
    def getyearvalues(self):
        self.getseacher()
        query_sql= config['reprotDesc']['values'] %(self.wheresql)
        applog.debug(query_sql)
        mss = mysql(curtype="dict")
        re =  mss.getAlldict(query_sql)
        applog.debug(re)
        mss.tearDown()
        result=[]
        flag =0
        temp={}
        rowsum=0
        i=0
        for row in re :
            #print(row)
            i=i+1            
            key = row.get('class_code')
            value = row.get('fee',0)
            C000=row.get('consume_date','')
               
            if flag== 0 :                
                temp['consume_date']=C000
                temp[key]=float('%0.02f' %(value))
                flag=C000
                rowsum=value
                #print(temp)
            elif  C000 != flag :
                temp['SUM']=float('%0.02f' %(rowsum))
                flag=C000
                C000=None
                rowsum=value
                #print(temp)
                result.append(temp)
                temp={} 
                temp[key]=float('%0.02f' %(value))
                temp['consume_date']=flag
                rowsum=value
            else:
                rowsum=rowsum+value
                temp[key]=float('%0.02f' %(value)) 
                #print(temp) 
                              
            if i == len(re) :
                temp['SUM']=float('%0.02f' %(rowsum))
                flag=C000
                C000=None
                rowsum=0
                #print(temp)
                result.append(temp)
                temp={} 
        summary={}           
        for dicta in result: 
            for (k, v) in dicta.items():
                if k != 'consume_date' :
                    summary[k]=float('%0.02f' %(summary.get(k,0)+v)) 
        summary['consume_date']='合计'
        applog.debug(summary)
        tt={}
        tt['summary']=[summary]
        tt['records']=result        
        return tt

class car_maintenance:
    def __init__(self,type,dict):
        self.length =0
        self.recid = dict.get('recid')
        if(self.recid is None):
            self.length =0
        else:
            self.length = len(self.recid)

        self.type =type
        self.recid = dict.get('record[recid]')
        self.date =dict.get('record[date]')
        self.mtl_name = dict.get('record[mtl_name]')
        self.odometer = dict.get('record[odometer]')
        self.remark = dict.get('record[remark]')
        self.records = []

    def getparam(self):
        if(self.length >0):
            for length in list(range(self.length)):
                if(self.type == 'add'):
                    self.records.append((self.date[length],self.mtl_name[length],self.odometer[length],self.remark[length]))
                elif(self.type == 'edit'):
                    self.records.append((self.date[length],self.mtl_name[length],self.odometer[length],self.remark[length],self.recid[length]))
                else:
                    pass
        return self.records

class tableFiled:
    '''
        set form list from tablefiled
    '''

    def __init__(self,fieldname):
        self.fieldname =fieldname


    def getTableField(self):
        query_sql= config['tableFiled'][self.fieldname]
        applog.debug(query_sql)
        mss = mysql(curtype="dict")
        re =  mss.getAlldict(query_sql)
        mss.tearDown()
        return re

class DateGrid:
    '''
        option grid table date  for
        insert table
        update table
        delete table

    '''
    def __init__(self,type,dict):
        self.tablename = dict.get('name')
        applog.debug(dict)
        self.type =type
        self.cmd =''.join(dict.get('cmd'))
        self.searchlogic = ''
        sl = dict.get('searchLogic')
        if (sl is not None):
            self.searchlogic = ''.join(sl)
        applog.debug(self.searchlogic)
        self.offest = 0
        self.limit  = 13
        self.sortfield ='recid'
        self.direction ='asc'
        self.wheresql =''
        wheresql1 = ''
        if ( self.cmd =='get-records'):
            self.offest   = (int)(''.join(dict.get('offset')))
            self.limit  = (int)(''.join(dict.get('limit')))
            if dict.get('sort[0][field]') is not None :
                self.sortfield = ''.join(dict.get('sort[0][field]'))
                self.direction = ''.join(dict.get('sort[0][direction]'))
            self.wheresql = ''


        for idx in range(len(dict)) :
            applog.debug(idx)
            ssearchfield_key = 'search[%s][field]' %(idx)
            searchvalue_key = 'search[%s][value]'  %(idx)
            opera_key = 'search[%s][operator]'  %(idx)
            if(dict.get(ssearchfield_key) is None):
                break
            else:
                ssearchfield = ''.join(dict.get(ssearchfield_key))
                searchvalue = ''.join(dict.get(searchvalue_key ))
                opera = ''.join(dict.get( opera_key))
                wheresql0 =''
                if (opera == 'is'):
                    operator ='='
                    wheresql0 = " %s  aa.%s = %r " %(self.searchlogic,ssearchfield,searchvalue)
                elif (opera == 'ends'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,'%'+searchvalue)
                elif (opera == 'begins'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,searchvalue+'%')
                elif (opera == 'contains'):
                    wheresql0 = " %s  aa.%s like %r  " %(self.searchlogic,ssearchfield,'%'+searchvalue+'%')
                else:
                    pass
            wheresql1 = wheresql1 + wheresql0
            applog.debug(wheresql0)
        self.wheresql = wheresql1
        applog.debug('seacher sql :%s'  %(self.wheresql))
        self.recid = None
        self.total = 0
        self.records=[]
        self.summary=[]
        self.param =[]
        if ( self.cmd =='delete-records'):
            self.recid = dict.get('selected[]')
        else:
            applog.debug(dict)
            objtable = config['classname'][self.tablename] #动态加载对象
            tabeobj = __import__('business') # import module
            c = getattr(tabeobj,objtable)
            self.param = c(self.type,dict).getparam()


    def getDateGrid2josn(self):
        mss = mysql(curtype="dict")
        query_sql = config['getgriddate'][self.tablename]  %(self.wheresql,self.sortfield,self.direction,self.offest,self.limit)
        applog.debug(query_sql)
        re =mss.getAlldict(query_sql)
        if (re is not None):
            self.records=re
        mss.tearDown()
        return self.records

    def getdateTotal_Summary(self):
        mss = mysql(curtype="dict")
        query_sql =  config['getgriddatecount'][self.tablename]  %(self.wheresql)
        applog.debug(query_sql)
        re =  mss.getOnedict(query_sql)
        if (re is not None):
            self.summary.append(re)
            self.total = self.summary[0].get('cc')
            applog.debug(self.summary.__len__())
        mss.tearDown()
        return self.summary

    def insertTable(self):
        exsql = config['addgriddate'][self.tablename]
        mss = mysql(curtype="")
        applog.debug(exsql ,self.param)
        re =  mss.exemany(exsql,self.param)
        mss.commit()
        mss.tearDown()
        return re

    def updateTable(self):
        exsql = config['editgriddate'][self.tablename]
        mss = mysql(curtype="")
        applog.debug(exsql,self.param)
        re =  mss.exemany(exsql,self.param)
        mss.commit()
        mss.tearDown()
        return re

    def defTable(self):
        exsql =  config['deletegriddate'][self.tablename]
        mss = mysql(curtype="")
        applog.debug(exsql)
        re =  mss.exemany(exsql,self.recid)
        mss.commit()
        mss.tearDown()
        return re

class CheackDate:
    def __init__(self,tablename,datetime):
        self.datetime = datetime
        self.tablename = tablename
    def cheaked(self):
        exsql = config['cheakede'][self.tablename] %(self.datetime)
        mss = mysql(curtype="")
        applog.debug(exsql)
        re =  mss.exesql(exsql)
        mss.commit()
        mss.tearDown()
        return re

class batabase:
    def __init__(self,dc):
        self.mysql = mysql('')
        #self.filename = ''.join(dc.get('record[filename][0][name]'))
        #self.content = dc.get('record[filename][0][content][0]')
                
    def backup(self): 
        #file_object = open('thefile.txt', 'w')
        #self.content._copy_file(file_object)               
        re = self.mysql.backUpDateBase()
        applog.debug(re)
        return re


    
def getPmonth(consume_date):
    if (consume_date is None):
        return ''
    format="%Y%m"
    t1=time.strptime( consume_date,format)
    returnformtat='%s%s'
    moth = t1.tm_mon-1
    year = t1.tm_year
    if (moth == 0):
        moth = 12
        year = year-1
    if (moth <10):
        returnformtat='%s0%s'
    return returnformtat %(year,moth)


def main():
    aa =tuple()

    applog.info("ddddd")
    return 0

if __name__ == '__main__':
    main()

