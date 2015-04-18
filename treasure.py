#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import sys
from core.info import Help
from core.libs.process import output
from core.libs.functions import utilities
from core.libs.enviroment import interactive

def main():

    s1 = utilities.sabc(1)
    s2 = utilities.sabc(2)
    s3 = utilities.sabc(3)
    s4 = utilities.sabc(4)

    if s1 is False:
        Help()
        
    try:

        if sys.argv[1] == '-h':
            Help()

        if sys.argv[1] == '-e' and s2 is True and sys.argv[3] == 'btc':
            output.BTCAddresses(sys.argv[2])

        if sys.argv[1] == 'hunt' and s2 is False and s3 is False:
            interactive.search()

        if sys.argv[1] == '-e' and s2 is True and sys.argv[3] == 'iat':
            output.InstagramAccessToken(sys.argv[2])

        if sys.argv[1] == '-e' and s2 is True and sys.argv[3] == 'ipv4':
            output.IPv4Addresses(sys.argv[2])

        if sys.argv[1] == '-e' and s2 is True and sys.argv[3] == 'ipv6':
            output.IPv6Addresses(sys.argv[2])

        if sys.argv[1] != '-e' and sys.argv[1] != 'hunt':
            Help()

        if sys.argv[1] == '-e' and s2 is False:
            Help()

        if sys.argv[3] != 'btc' and sys.argv[3] != 'iat' and sys.argv[3] != 'ipv4' and sys.argv[3] != 'ipv6':
            Help()

    except IndexError:
        pass

if __name__ == "__main__":
    main()
