# Treasure
Hunt for sensitive information on github.

Dependencies:
-------------
1. bs4
2. requests

Explanation:
------------
- Once you perform a search a *.code.dump file will be made within your current working containing all of the code that your search has provided.

Installation:
-------------
    sudo ./install [NAME]
- [NAME] is the System link name used to reference Treasure by when running it from a different directory.

Usage:
------

    ./treasure.py hunt | interactively search for code.

    ./treasure.py ssh [USERNAME] | Grab a users Public SSH Key(s) if available.

    ./treasure.py -e [FILE] iat     | Grab instagram access tokens.

    ./treasure.py -e [FILE] ipv4    | Grab ipv4 addresses.

    ./treasure.py -e [FILE] ipv6    | Grab ipv6 addresses.

    ./treasure.py -e [FILE] btc     | Grab bitcoin wallet addresses.

    What can it extract from your code dump ?

    - ipv4, ipv6 addresses
    - instagram access tokens
    - bitcoin wallet addresses

Donations:
----------
1. 17vorVqtJqbDaN6ZC6UGE7UwGC4QVmDNMh

Guerrilla Warfare Free License ("GWFL"):
----------------------------------------

1. You're free to modify this software to YOUR liking or leave it as is.

2. This software comes as is, and may or may not receive any additional updates.

3. The initial download and use of this software constitutes that you adhere and comply to the writing of this end user license agreement (EULA).

4. The Developer is NOT at ALL under any circumstances responsible for YOUR actions or the actions of any other third part instances that may use this software for any illegal or nefarious activities.
