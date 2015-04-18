#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re

class EXTRACTIONOPERATIONS():

    def InstagramAccessTokens(self, fwiat):

        found = []
        tokensrch = re.compile(r'[0-9]{7,10}\.[0-9a-f]{5,8}\.[0-9a-f]{32}')
        with open(fwiat, 'rb') as FileWithAccessToken:
            for token in FileWithAccessToken:
                token = token.replace('\n', '')
                if tokensrch.findall(token):
                    found.append(token)

        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique link(s)
        return u.keys()

    # Grab Bitcoin Wallet Addresses
    def BitcoinWalletAddress(self, fwbw):

        found = [] # List of found bitcoin wallet addresses
        btcwsrch = re.compile(r'(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,30}(?![a-km-zA-HJ-NP-Z0-9])|(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{33,35}(?![a-km-zA-HJ-NP-Z0-9])')
        with open(fwbw, 'rb') as FileWithBitcoinAddress:
            for wallet in FileWithBitcoinAddress:
                wallet = wallet.replace('\n', '')
                if btcwsrch.findall(wallet):
                    found.append(wallet)

        # remove duplicate link elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique link(s)
        return u.keys()

    def IPv6Addresses(self, fowipv6):

        found = [] # List of found ipv6 numbers

        ipv6srch = re.compile(r"^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$")

        with open(fowipv6, 'rb') as FileWithCCN:
            for line in FileWithCCN:
                ipv6addr = line.replace('\n', '')
                if ipv6srch.findall(ipv6addr):
                    found.append(ipv6addr)

        # remove duplicate ipv6 elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique ssn numbers
        return u.keys()

    def IPv4Addresses(self, foi):

        found = [] # List of found ipv4 addresses
        ipv4srch = re.compile(r'([0-9]+)(?:\.[0-9]+){3}')

        with open(foi, 'rb') as FileWithIPv4:
            for line in FileWithIPv4:
                ipv4 = line.replace('\n', '')
                if ipv4srch.findall(ipv4):
                    found.append(ipv4)

        # remove duplicate ipv4 elements
        u = {}
        for item in found:
            u[item] = 1

        #returns a list of unique ipv4 addresses
        return u.keys()

extract = EXTRACTIONOPERATIONS()
