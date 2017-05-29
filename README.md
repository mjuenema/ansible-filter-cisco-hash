# ansible-filter-cisco-hash

Ansible Jinja2 filters for Cisco type 5 and type 7 password hashes. This requires the [passlib](https://pypi.python.org/pypi/passlib) Python library.

Example:

```
vars:
  enable_password: my_enable_password
  user_password: my_user_password

ios_config:
  lines: 
  - "enable password 5 {{enable_passowrd|ciscohash5}}" 
  - "user my_username password 7 {{user_password|ciscohash7}}"
```

A big thanks goes to Jon Langemak for the [Creating your own Ansible filter plugins](http://www.dasblinkenlichten.com/creating-ansible-filter-plugins/) page. It flashed a bright light on the subject ;-)

Markus J&uuml;nemann, May 2017
