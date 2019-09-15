#!/usr/bin/env python

import packaging.version

import passlib
import passlib.hash

# Version 1.7.0 introduced major changes to the `passlib.hash` API.
PASSLIB_VERSION = packaging.version.parse(passlib.__version__)
PASSLIB_API_CHANGE_VERSION = packaging.version.parse('1.7.0')

try:
    MD5_CRYPT_USING=True
except AttributeError:
    MD5_CRYPT_USING=False


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
        if PASSLIB_VERSION >= PASSLIB_API_CHANGE_VERSION:
            return passlib.hash.md5_crypt.using(salt_size=4).hash(password)
        else:
            return passlib.hash.md5_crypt.encrypt(password, salt_size=4)

    def ciscohash7(self, password, salt=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_type7.html"""
        if salt != '':
            if PASSLIB_VERSION >= PASSLIB_API_CHANGE_VERSION:
                return passlib.hash.cisco_type7.using(salt=salt).hash(password)
            else:
                return passlib.hash.cisco_type7.using(salt=salt).encrypt(password)
        else:
            if PASSLIB_VERSION >= PASSLIB_API_CHANGE_VERSION:
                return passlib.hash.cisco_type7.hash(password)
            else:
                return passlib.hash.cisco_type7.encrypt(password)

    def ciscohashpix(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_pix.html"""
        if PASSLIB_VERSION >= PASSLIB_API_CHANGE_VERSION:
            return passlib.hash.cisco_pix.hash(password, user)
        else:
            return passlib.hash.cisco_pix.encrypt(password, user)

    def ciscohashasa(self, password, user=''):
        """https://passlib.readthedocs.io/en/stable/lib/passlib.hash.cisco_asa.html"""
        if PASSLIB_VERSION >= PASSLIB_API_CHANGE_VERSION:
            return passlib.hash.cisco_asa.hash(password, user)
        else:
            raise NotImplementedError('Cisco ASA Hash was added in Passlib 1.7')


