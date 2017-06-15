[![Travis master branch](https://img.shields.io/travis/mjuenema/ansible-filter-cisco-hash/master.svg?style=flat-square)](https://travis-ci.org/mjuenema/ansible-filter-cisco-hash/branches)
[![Travis develop branch](https://img.shields.io/travis/mjuenema/ansible-filter-cisco-hash/develop.svg?style=flat-square)](https://travis-ci.org/mjuenema/ansible-filter-cisco-hash/branches)
[![GitHub release](https://img.shields.io/github/release/mjuenema/ansible-plugin-cisco-hash.svg?style=flat-square)](https://github.com/mjuenema/ansible-filter-cisco-hash/releases)


# ansible-filter-cisco-hash

Ansible Jinja2 filters for Cisco type 5 and type 7 password hashes.
This requires the [Passlib](https://pypi.python.org/pypi/passlib) Python library.

* `{{password|ciscohash5}}` (see Note)
* `{{password|ciscohash7}}`
* `{{password|ciscohashpix}}`
* `{{password|ciscohashpix(user)}}`
* `{{password|ciscohashpasa}}` (only with Passlib 1.7 or later)
* `{{password|ciscohashasa(user)}}` (only with Passlib 1.7 or later)

*Note: Because the hash will be different at each invocation one has to
add a *when* condition to the task as shown in the example below.*

The filter plugin works with Ansible 2.0+ and Passlib 1.6+.

## Usage

The filters are wrapped into an Ansible role which can be installed directly
from Github.

```
pip install passlib
ansible-galaxy install -f git+https://github.com/mjuenema/ansible-filter-cisco-hash.git
```

The role does not contain any playbooks but once you reference in your own
playbook the filters become available.

## Example

```
- name: Configure Cisco IOS
  hosts: routers

  vars:
    enable_password: my_enable_password

  roles:
    - ansible-filter-cisco-hash

  tasks:
    - name: Configure enable secret
      ios_config:
        lines:
        - "enable secret 5 {{enable_password|ciscohash5}}"
      when: 'enable secret 5' not in ansible_net_config
```

A big thanks goes to Jon Langemak for the [Creating your own Ansible filter
plugins](http://www.dasblinkenlichten.com/creating-ansible-filter-plugins/)
page.

Markus J&uuml;nemann, May 2017
