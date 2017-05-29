#!/usr/bin/env python
from jinja2 import Environment, Template, DictLoader
import passlib.hash
import filterciscohash

TEMPLATES = {
        'ciscohash5_template': '{{password|ciscohash5}}',
        'ciscohash7_template': '{{password|ciscohash7}}',
        'ciscohashasa_template': '{{password|ciscohashasa}}',
        'ciscohashasa_user_template': '{{password|ciscohashasa(user)}}',
        'ciscohashpix_template': '{{password|ciscohashpix}}',
        'ciscohashpix_user_template': '{{password|ciscohashpix(user)}}'
        }

PASSWORD='password'
USER='user'

environment = Environment(loader=DictLoader(TEMPLATES))
environment.filters['ciscohash5'] =  filterciscohash.FilterModule().ciscohash5
environment.filters['ciscohash7'] =  filterciscohash.FilterModule().ciscohash7
environment.filters['ciscohashasa'] =  filterciscohash.FilterModule().ciscohashasa
environment.filters['ciscohashpix'] =  filterciscohash.FilterModule().ciscohashpix

PASSWORD='password'

def test_ciscohash5():
    assert passlib.hash.md5_crypt.verify(PASSWORD, filterciscohash.FilterModule().ciscohash5(PASSWORD))

def test_ciscohash5_jinja2():
    template = environment.get_template('ciscohash5_template')
    assert template.render(password=PASSWORD).startswith('$1$')


def test_ciscohash7():
    assert passlib.hash.cisco_type7.decode(filterciscohash.FilterModule().ciscohash7(PASSWORD)) == PASSWORD

def test_ciscohash7_jinja2():
    template = environment.get_template('ciscohash7_template')
    assert len(template.render(password=PASSWORD)) == 18


def test_ciscohashasa():
    assert passlib.hash.cisco_asa.verify(PASSWORD, filterciscohash.FilterModule().ciscohashasa(PASSWORD))

def test_ciscohashasa_jinja2():
    template = environment.get_template('ciscohashasa_template')
    assert template.render(password=PASSWORD) == 'NuLKvvWGg.x9HEKO'

def test_ciscohashasa_user():
    assert passlib.hash.cisco_pix.verify(PASSWORD, filterciscohash.FilterModule().ciscohashpix(PASSWORD, USER), user=USER)

def test_ciscohashasa_user_jinja2():
    template = environment.get_template('ciscohashasa_user_template')
    assert template.render(password=PASSWORD, user=USER) == 'A5XOy94YKDPXCo7U'


def test_ciscohashpix():
    assert passlib.hash.cisco_pix.verify(PASSWORD, filterciscohash.FilterModule().ciscohashpix(PASSWORD))

def test_ciscohashpix_jinja2():
    template = environment.get_template('ciscohashpix_template')
    assert template.render(password=PASSWORD) == 'NuLKvvWGg.x9HEKO'

def test_ciscohashpix_user():
    assert passlib.hash.cisco_pix.verify(PASSWORD, filterciscohash.FilterModule().ciscohashpix(PASSWORD, USER), user=USER)

def test_ciscohashpix_user_jinja2():
    template = environment.get_template('ciscohashpix_user_template')
    assert template.render(password=PASSWORD, user=USER) == 'A5XOy94YKDPXCo7U'
