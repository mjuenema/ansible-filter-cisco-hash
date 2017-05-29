#!/usr/bin/env python

import passlib.hash

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
        return passlib.hash.md5_crypt.using(salt_size=4).hash(password)

    def ciscohash7(self, password):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html"""
        return str(passlib.hash.cisco_type7.hash(password))

    def ciscohashpix(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html"""
        return str(passlib.hash.cisco_pix.hash(password, user))

    def ciscohashasa(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html"""
        return str(passlib.hash.cisco_asa.hash(password, user))


