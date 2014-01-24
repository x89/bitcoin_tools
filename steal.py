#!/usr/bin/env python
# Python 3.3 code following.

import dns.resolver
from time import sleep
import sys

# List of DNS servers and how frequently they update
class BitcoinDNSServer:
    def __init__(self, host, delay=60):
        self.host = host
        self.original_delay = delay
        self.delay = delay
    
    def get_addresses(self, seconds_that_have_passed):
        if (seconds_that_have_passed - self.delay) > 0 \
            or seconds_that_have_passed == 0:
            addresses = dns.resolver.query(self.host)
            self.delay += self.original_delay
            return [a.address for a in addresses]
        else:
            return False

servers = (
    BitcoinDNSServer('seed.bitcoin.sipa.be'),
    BitcoinDNSServer('dnsseed.bluematt.me', delay=90),
    BitcoinDNSServer('dnsseed.bitcoin.dashjr.org'),
    BitcoinDNSServer('seed.bitcoinstats.com'),
    BitcoinDNSServer('bitseed.xf2.org', delay=3200), # This one may be static?
)

zero_time = 0
bitcoin_ips = set()
while(1):
    try:
        for server in servers:
            try: addresses = server.get_addresses(zero_time)
            except: pass
            if addresses:
                bitcoin_ips |= set(addresses)
                print(zero_time, server.host, len(addresses))
        zero_time += 1
        sleep(1)
    except KeyboardInterrupt:
        print(bitcoin_ips)
        sys.exit()
