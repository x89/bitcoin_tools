#!/usr/bin/env python
# Python 3.3 code following.
# See: https://github.com/bitcoin/bitcoin/blob/master/src/chainparams.cpp#L143

import dns.resolver

# List of DNS servers and how frequently they update
class BitcoinDNSServer:
    def __init__(self, host, delay=60):
        self.host = host
    
    def get_addresses(self):
        addresses = dns.resolver.query(self.host)
        return [a.address for a in addresses]

servers = (
    BitcoinDNSServer('seed.bitcoin.sipa.be'),
    BitcoinDNSServer('dnsseed.bluematt.me'),
    BitcoinDNSServer('dnsseed.bitcoin.dashjr.org'),
    BitcoinDNSServer('seed.bitcoinstats.com'),
    BitcoinDNSServer('bitseed.xf2.org'), # This one may be static?
)

bitcoin_ips = set()
for server in servers:
    addresses = server.get_addresses()
    if addresses:
        bitcoin_ips |= set(addresses)

print(bitcoin_ips)
for ip in bitcoin_ips:
    print(ip)
