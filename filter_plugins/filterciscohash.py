#!/usr/bin/env python

import passlib.hash

# Version 1.7.0 introduced `passlib.hash.md5_crypt.using(salt_size=...)`.
try:
    md5_crypt = passlib.hash.md5_crypt.using
except AttributeError:
    md5_crypt = passlib.hash.md5_crypt

class FilterModule(object):
    def filters(self):
        return {
            'ciscohash5': self.ciscohash5,
            'ciscohash7': self.ciscohash7,
            'ciscohashpix': self.ciscohashpix,
            'ciscohashasa': self.ciscohashasa
        }

    def ciscohash5(self, password):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.md5_crypt.html"""
        return md5_crypt(salt_size=4).hash(password)

    def ciscohash7(self, password):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html"""
        return passlib.hash.cisco_type7.hash(password)

    def ciscohashpix(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html"""
        return passlib.hash.cisco_pix.hash(password, user)

    def ciscohashasa(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html"""
        return passlib.hash.cisco_asa.hash(password, user)


