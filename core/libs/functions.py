#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import os
import sys

# Dependency imports
import requests

# Global user agent to use.
GLOBALUSERAGENT = {"User-Agent":"Mozilla/5.0 (X11; Linux x86; rv:37.0) Gecko/20100101 Firefox/1000.0"}

class Utilities():

    #Get Request
    def GetHTTPRequest(self, url):
        GetRequestSession = requests.Session()
        response = GetRequestSession.get(url, headers=GLOBALUSERAGENT)
        return response # Just return the object, not the content.

    def GetHTTPostRequest(self, url, data):
        GetRequestSession = requests.Session()
        response = GetRequestSession.get(url, params=data, headers=GLOBALUSERAGENT)
        return response # Just return the object, not the content.

    def pi(self, pdata=''):
        print pdata

    # sys.argv bool checks for assurance.
    def sabc(self, argnum):
        try:
            if sys.argv[argnum]:
                return True
        except Exception:
            return False

    # Useful for interactive operations
    def select(self, message):
        while True:
            select = raw_input("\n{}".format(message))
            return select

    # String boolean self-check.
    def sbc(self, fn, s): # Check if string is in a file.
        #return a NoneType if the string is not in the file.
        #.readlines() May be a problem is database files get too large.

        if os.path.exists(fn) is False:
            MakeFile = open(fn, 'a').close()

        if os.path.exists(fn) is True:
            pass

        f = open(fn, 'r')
        f = f.readlines()
        for i in f:
            i = i.replace("\n", '')
            if s.decode('utf-8').encode('utf-8') in i:
                return True

utilities = Utilities()
