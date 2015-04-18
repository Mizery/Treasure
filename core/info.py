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

    ./treasure.py hunt                | interactively search for code.

    ./treasure.py -e [FILE] [CONTENT] | extract desired infromation from your code dump.

    ./treasure.py -e [FILE] iat     | Grab instagram access tokens.

    ./treasure.py -e [FILE] ipv4    | Grab ipv4 addresses.

    ./treasure.py -e [FILE] ipv6    | Grab ipv6 addresses.

    ./treasure.py -e [FILE] btc     | Grab bitcoin wallet addresses.

    What can it extract from your code dump ?

    - ipv4, ipv6 addresses
    - instagram access tokens
    - bitcoin wallet addresses
    """
