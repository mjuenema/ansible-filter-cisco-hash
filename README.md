# ansible-filter-cisco-hash

Ansible Jinja2 filters for Cisco type 5 and type 7 password hashes.
This requires the [passlib](https://pypi.python.org/pypi/passlib) Python library.

* `{{password|ciscohash5}}` (see Note)
* `{{password|ciscohash7}}`
* `{{password|ciscohashpix}}`
* `{{password|ciscohashpix(user)}}`
* `{{password|ciscohashpasa}}`
* `{{password|ciscohashasa(user)}}`

*Note: Because the hash will be different at each invocation one has
add a *when* condition to the task as shown in the example below.*

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
    user_password: my_user_password

  roles:
    - ansible-filter-cisco-hash

  tasks:
    - name: Configure enable secret
      ios_config:
        lines: 
        - "enable secret 5 {{enable_passowrd|ciscohash5}}" 
      when: 'enable secret 5' not in ansible_net_config
```

A big thanks goes to Jon Langemak for the [Creating your own Ansible filter
plugins](http://www.dasblinkenlichten.com/creating-ansible-filter-plugins/)
page.

Markus J&uuml;nemann, May 2017
