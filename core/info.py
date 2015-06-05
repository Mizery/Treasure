#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

from core.libs.paint import colors

class ColoredOutPut():

    # Info variables
    INFO = colors.W+'[INFO]'+colors.N + ": "
    ERROR = colors.R+'[ERROR]'+colors.N + ": "
    FAIL = colors.R+'[FAIL]'+colors.N + ": "
    FOUND = colors.W+'[FOUND]'+colors.N + ": "
    STATUS = colors.Y+"[RESULTS]"+colors.N+": "

notifications = ColoredOutPut()

def Help():

    print """
    [GWF Certified] - https://twitter.com/GuerrillaWF

    ./treasure.py hunt | interactively search for something.

    ./treasure.py ssh [USERNAME] | Grab a users Public SSH Key(s) if available.

    ./treasure.py -e [FILE] iat  | Grab instagram access tokens.

    ./treasure.py -e [FILE] ipv4 | Grab ipv4 addresses.

    ./treasure.py -e [FILE] ipv6 | Grab ipv6 addresses.

    ./treasure.py -e [FILE] btc | Grab bitcoin wallet addresses.

    ./treasure.py -e [FILE] bid | Grab blockchain identifiers.

    ./treasure.py -e [FILE] fat | Grab facebook accesst tokens.
    """
