#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

import re
from extraction import extract
from functions import utilities
from core.info import notifications

class PROCESSEXTRACT():

    def InstagramAccessToken(self, file):
        IATExtract = extract.InstagramAccessTokens(file) # Collected emails

        if len(IATExtract) is 0:
            utilities.pi("{}No Instagram access tokens in {}".format(notifications.FAIL, file))

        if len(IATExtract) > 0: # legit file, containing at least 1 email address.
            FoundIATs = [] # Re-filter, so you get exactly what you're looking for.
            for instance in IATExtract:
                IATRegex = re.compile(r'[0-9]{7,10}\.[0-9a-f]{5,8}\.[0-9a-f]{32}')
                IATContainer = IATRegex.search(instance)
                IATs = IATContainer.group()
                FoundIATs.append(IATs)
            UOD = {}
            for item in FoundIATs:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------------------------")
            utilities.pi("      EXTRACTED Instagram access tokens     ")
            utilities.pi("--------------------------------------------")
            count = 0
            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} instagram access token from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} instagram access tokens from {}\n".format(str(count), file))

    def IPv6Addresses(self, file):
        IPv6Extract = extract.IPv6Addresses(file)

        if len(IPv6Extract) is 0:
            utilities.pi("{}No IPv6 addresses in {}".format(notifications.FAIL, file))

        if len(IPv6Extract) > 0: # legit file, containing at least 1 ipv6 number.
            FoundIPV6s = [] # Re-filter, so you get exactly what you're looking for.
            for instance in IPv6Extract:
                IPv6Regex = re.compile(r'^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$')
                IPv6List = IPv6Regex.search(instance)
                IPv6s = IPv6List.group()
                FoundIPV6s.append(IPv6s)

            UOD = {}
            for item in FoundIPV6s:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------")
            utilities.pi("      EXTRACTED IPv6s     ")
            utilities.pi("--------------------------")
            count = 0

            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} IPv6 address from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} IPv6 addresses from {}\n".format(str(count), file))

    def IPv4Addresses(self, file):
        IPv4Extract = extract.IPv4Addresses(file) # Collected ipv4s

        if len(IPv4Extract) is 0:
            utilities.pi("{}No IPv4 addresses in {}".format(notifications.FAIL, file))

        if len(IPv4Extract) > 0: # legit file, containing at least 1 ipv4 address.
            FoundIPv4s = [] # Re-filter, so you get exactly what you're looking for.
            for instance in IPv4Extract:
                IPv4Regex = re.compile(r'([0-9]+)(?:\.[0-9]+){3}')
                IPv4Container = IPv4Regex.search(instance)
                IPv4s = IPv4Container.group()
                FoundIPv4s.append(IPv4s)
            UOD = {}
            for item in FoundIPv4s:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------")
            utilities.pi("      EXTRACTED IPV4s     ")
            utilities.pi("--------------------------")
            count = 0
            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} IPv4 address from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} IPv4 addresses from {}\n".format(str(count), file))

    def BTCAddresses(self, file):
        BTCWAExtract = extract.BitcoinWalletAddress(file)

        if len(BTCWAExtract) is 0:
            utilities.pi("{}No Bitcoin addresses in {}".format(notifications.FAIL, file))

        if len(BTCWAExtract) > 0: # legit file, containing at least 1 link.
            FoundWallets = [] # Re-filter, so you get exactly what you're looking for.

            for instance in BTCWAExtract:
                BTCWalletRegex = re.compile(r'(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,30}(?![a-km-zA-HJ-NP-Z0-9])|(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{33,35}(?![a-km-zA-HJ-NP-Z0-9])')
                wallet = BTCWalletRegex.findall(instance)
                for address in wallet: FoundWallets.append(address)
            UOD = {}
            for item in FoundWallets:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------")
            utilities.pi("  EXTRACTED BTC Addresses ")
            utilities.pi("--------------------------")
            count = 0
            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Bitcoin address from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Bitcoin addresses from {}\n".format(str(count), file))

    def FacebookAccessTokens(self, file):
        FATExtract = extract.FacebookAccessTokens(file)

        if len(FATExtract) is 0:
            utilities.pi("{}No Facebook Access Tokens in {}".format(notifications.FAIL, file))

        if len(FATExtract) > 0:
            FoundFATs = [] # Re-filter, so you get exactly what you're looking for.
            for instance in FATExtract:
                FATRegex = re.compile(r'(access_token\=[0-9]{15}\|(.*){27})')
                FATList = FATRegex.search(instance)
                FATs = FATList.group()
                FoundFATs.append(FATs)

            UOD = {}
            for item in FoundFATs:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------")
            utilities.pi("  Facebook Access Tokens  ")
            utilities.pi("--------------------------")
            count = 0

            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Facebook Access Token from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Facebook Access Tokens from {}\n".format(str(count), file))

    def BlockchainIdentifiers(self, file):
        BCIDSExtract = extract.BlockchainIdentifiers(file)
        if len(BCIDSExtract) is 0:
            utilities.pi("{}No Blockchain Identifiers in {}".format(notifications.FAIL, file))

        if len(BCIDSExtract) > 0:
            FoundBCIDS = [] # Re-filter, so you get exactly what you're looking for.
            for instance in BCIDSExtract:
                BCIDSRegex = re.compile(r'[0-9a-f]{5,8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{5,13}')
                BCIDSList = BCIDSRegex.search(instance)
                BCIDSs = BCIDSList.group()
                FoundBCIDS.append(BCIDSs)

            UOD = {}
            for item in FoundBCIDS:
                UOD[item] = 1
            keys = UOD.keys()
            utilities.pi("--------------------------")
            utilities.pi("  Blockchain Identifiers  ")
            utilities.pi("--------------------------")
            count = 0

            for output in keys:
                count += 1
                utilities.pi(notifications.INFO + output)

            if count is 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Blockchain Identifier from {}\n".format(str(count), file))

            elif count > 1:
                utilities.pi("\n" + notifications.STATUS + "Extracted {} Blockchain Identifiers from {}\n".format(str(count), file))

output = PROCESSEXTRACT()
