#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
import os
import sys
from bs4 import BeautifulSoup
#from extraction import extract | For later.
from functions import utilities
from core.libs.paint import colors
from core.info import notifications

class SearchOperations():

    # Offset of path component to delete when converting to raw
    REM_OFFSET = 2
    RAWBASE = "https://raw.github.com/"
    SEARCH = "https://github.com/search"

    def extract(self, data):
        s = BeautifulSoup(data)
        for i in s.findAll("p", {"class":"title"}):
            p = i.findAll("a")
            # The second link is the reference ...
            yield p[1].get("href")

    def is_last_page(self, data):
        s = BeautifulSoup(data)
        if s.find("p", {"class":"title"}):
            return False
        else:
            return True

    def raw_url(self, p):
        p = p.strip("/")
        parts = p.split("/")
        del parts[searchfor.REM_OFFSET]
        return searchfor.RAWBASE + "/".join(parts)

    def make_fname(self, p):
        p = p.strip("/")
        parts = p.split("/")
        return parts[0] + "." + parts[1]

    def code(self, query, listonly=False):
        if query == 'q':
            utilities.pi('{}Exiting Treasure ...'.format(notifications.INFO))
            exit(0)

        elif query == '' or query == ' ':
            utilities.pi(' {} Empty code searches are not allowed.'.format(notifications.ERROR))
            exit(0)

        utilities.pi("\n {}Hunting for {}".format(notifications.INFO, query))

        page = 1
        breakpoint = 1
        while breakpoint == 1:
            params = dict(
                q = query,
                type = "Code",
                p = page
                )

            r = utilities.GetHTTPostRequest(searchfor.SEARCH, params)
            if searchfor.is_last_page(r.content):
                utilities.pi('** No more results for {} **'.format(query))
                breakpoint = 1 # Break the while loop.
                break
            for u in searchfor.extract(r.content):
                ru = searchfor.raw_url(u)
                if listonly:
                    print ru
                else:
                    fn = searchfor.make_fname(u)
                    ret = utilities.GetHTTPRequest(ru)
                    if ret.status_code == 200:
                        codedumppath = '{}.code.dump'.format(query.replace(' ', '_'))
                        # Print output
                        utilities.pi(" {}".format(notifications.FOUND) + ru.split('/')[-1] + " " + "from {}".format(ru.split('/')[3]))
                        with open(codedumppath, "a+") as file:
                            cb = utilities.sbc(codedumppath, ret.content.decode('utf-8'))
                            if cb is None:
                                file.write(ret.content + '\n')
                                file.close()

                            elif cb is True:
                                pass
                    else:
                        pass
            page += 1

searchfor = SearchOperations()

class Enviroment():

    def search(self):
        utilities.pi("""
 #######################################################
 #                                                     #
 #              """+colors.Y+"""Treasure"""+colors.N+""" - """+colors.G+"""HUNT"""+colors.N+""" """+colors.B+"""for"""+colors.N+""" """+colors.W+"""CODE"""+colors.N+"""               #
 #           Type q or ^C to exit """+colors.Y+"""Treasure"""+colors.N+"""             #
 #                                                     #
 # """+colors.R+"""Help ?"""+colors.N+""":                                             #
 # """+colors.C+"""1. https://help.github.com/articles/searching-code/"""+colors.N+""" #
 #                                                     #
 #######################################################""")

        breakpoint = 0 # Break point for the while loop.
        while breakpoint == 0:
            try:
                choice = utilities.select(" search|code: ")
                searchfor.code(choice)
            except KeyboardInterrupt:
                breakpoint == 1
                utilities.pi("\n{}Exiting Treasure ...".format(notifications.INFO))
                break

interactive = Enviroment()
