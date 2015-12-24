#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


import logging  
import logging.config
import configparser
import base64

logging.config.fileConfig('./config/logging.conf')
applog = logging.getLogger('easyWeb')


config = configparser.RawConfigParser()
config.sections()
config.read('./config/paramsqlist.ini','utf-8')

    #dsn = config['oracle_database']['DSN']
    #logger.debug("DSN:%s",dsn)


        
                
def main():
    copyright = 'admim'
    #转成bytes string
    bytesString = copyright.encode(encoding="utf-8")
    applog.info(bytesString)

    #base64 编码
    encodestr = base64.b64encode(bytesString)
    applog.info(encodestr)
    applog.info(encodestr.decode())

    #解码
    decodestr = base64.b64decode(encodestr)
    applog.info(decodestr.decode())


if __name__ == '__main__':
    main()

