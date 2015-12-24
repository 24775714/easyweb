#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

import os,sys
from business import DateGrid,sidebarnodes,panleTabsTabs,tableFiled,CheackDate,userinfo,batabase,year_report
from bottle import *
from seting import applog
import json

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

@route('/favicon.ico')
def favicon_set():
	  return static_file('favicon.ico', root='images', mimetype='image/ico')
#pci file
@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

#video file
@route('/video/<filename:re:.*\.3gp>')
def video_file(filename):
    return static_file(filename, root='./download',mimetype='video/3gpp')


#js script file
@route('/js/<filepath:path>')
def server_static_js(filepath):
    return static_file(filepath, root='js')

#js script file
@route('/download/<filepath:path>')
def static_fele(filepath):
    return static_file(filepath, root='./download/files')



@route('/')
@view('main_layout')
def index():
    return dict()

        
@route('/login2' , method='POST')
def login2():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        dc = request.POST.decode('utf-8').dict
        applog.debug(dc)
        rs={'status':'error',}
        user = userinfo('',dc)    
        if user.login() :   
            dc={}        
            nodes = sidebarnodes('',dc).getSidebarAll()
            rs['status']='success'
            rs['nodes']=nodes
        else:
            rs['message']="用户名或密码错误，请重新登录。"
        return rs
    else:
        return 'This is a normal request' 


@route('/showTabs/<tabid>')
def showPanleTabs(tabid):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        scode=tabid
        if (scode == 'tab0'):
            return template('maincontent')
        elif (scode == 'DES_REPORT'):
            tplnames = panleTabsTabs(scode,'').showTabsTemplate()
            filds = panleTabsTabs(scode,'').desc_reprot()
            #filds.insert(0,{ 'field': 'recid', 'caption': 'ID', 'size': '50px','sortable': 'true'})
            applog.debug('%s,%s' %(tplnames,scode))
            applog.debug(filds)
            return  template(tplnames[0],id=scode,table=tplnames[1],columns=filds)

        else:
            tplnames = panleTabsTabs(scode,'').showTabsTemplate()
            applog.debug('%s,%s' %(tplnames,scode))
            return  template(tplnames[0],id=scode,table=tplnames[1])
    else:
        return 'This is a normal request'


## get grid form  calss_id 填写表单中list数据
@route('/DataForm/<fieldname>')
def DataForm(fieldname):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        josoindate = {}
        re  = tableFiled(fieldname).getTableField()
        josoindate['items']=re
        josoindate['status']='success'
        return josoindate
    else:
        return 'This is a normal request'


### 填充 数据  、delete table  、 inset table  update table
@route('/data/<type>/<tablename>' , method='POST')
def optDateGrid(type,tablename):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        dc = request.POST.decode('utf-8').dict
        dc['name']=tablename
        applog.info(dc)
        obj=DateGrid(type,dc)
        reslutMsg = {"status":'error', "message":""}
        try:
            if (type == 'get'):
                redate={}
                recodes = obj.getDateGrid2josn()
                summary = obj.getdateTotal_Summary()
                if (recodes is not None):
                    redate['records'] = recodes
                    redate['total']=obj.total
                if (len(summary[0])>1):
                    redate['summary'] =summary
                applog.debug(redate)
                return  redate
            elif (type == 'delete'):
                re  = obj.defTable()
                if (re is None or re ==0 ):
                    reslutMsg["message"]="没有可删除的数据,请核对数据！"
                else:
                    reslutMsg["message"]=" 成功删除 %s 行！ "  %(re)
            elif (type == 'add'):    ###add  edit
                re = obj.insertTable()
                reslutMsg["message"]=" 成功新增  %s 行！ "  %(re)
            elif (type == 'edit'):
                re = obj.updateTable()
                reslutMsg["message"]=" 成功更新  %s 行！ "  %(re)
            else:
                reslutMsg["message"]=" args errs"
            return  reslutMsg
        except Exception  as ee:
            reslutMsg["message"]=ee
            return  reslutMsg



## 结算消费详单
@route('/checkreport/<table>/<datetime>' , method='POST')
def checkreport(table,datetime):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            obj = CheackDate(table,datetime)
            re  = obj.cheaked()
            return  '%s rows checked sucessful'  %(re)
        except Exception as err:
            return  'erro : %s'  %(str(err))

## 报表数据填充
@route('/descreport/<table>', method='POST' )
def descreport(table):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            dc = request.POST.decode('utf-8').dict
            dc['name']=table
            applog.debug(dc)
            obj = year_report(table,dc)
            re  = obj.getyearvalues()
            applog.debug(re)
            return re
        except Exception as err:
            applog.exception(err)
            return  'erro : %s'  %(str(err))

@route('/database/<type>', method='POST')
def database(type):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        applog.debug(type)
        dc = request.POST.decode('utf-8').dict
        applog.debug(dc)
        df = batabase(dc)
        str1 = df.backup()
        applog.debug(str1)
        return {"status":'error','message':'备份成功！！'}    
        
        
    
@route('/iso')
def get_iso():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        dc = request.POST.decode('utf-8').dict
        response.charset = 'ISO-8859-15'
        applog.debug(dc)
        return {'status':'sucessful'}

@route('/chart')
def get_test():
    applog.debug("test")
    return template('maincontent')
@route('/htmlcode/view')
def view_code():
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        applog.debug("test")
        return template('charthtml')


if __name__ == "__main__":
    # Interactive mode
    run(host='0.0.0.0',server='cherrypy',reloader=True,debug=True,port=8081)


 


