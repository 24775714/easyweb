#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os

if ( os.name == 'posix' ):
	pwdpath=os.getcwd()
elif (os.name == 'nt'):
	pwdpath=os.getcwd()
sys.path = [pwdpath] + sys.path
os.chdir(os.path.dirname(__file__))

import easyapp, bottle
application = bottle.default_app()


