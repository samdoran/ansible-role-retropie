#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes, to_native

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
---
module:
author:
    - Sam Doran (@samdoran)
version_added: '2.9'
short_description:
notes: []
description:
    -
options:
    opt1:
        description: []
"""

EXAMPLES = """
"""

RETURN = """
"""


def get_locale(module):
    rc, out, err = module.run_command('locale')
    locale = {}
    for line in out.splitlines():
        k, v = line.split('=')
        locale[k.lower()] = v.strip('"')
    return locale


def main():
    module = AnsibleModule(
        argument_spec={
            'lc_all': {'type': 'str', 'default': 'en_US.UTF-8'},
            'lang': {'type': 'str', 'default': 'en_US.UTF-8'},
            'language': {'type': 'str', 'default': 'en_US.UTF-8'},
        },
        supports_check_mode=True,
    )

    results = {
        'changed': False,
    }
    locale = get_locale(module)

    for k, v in sorted(module.params.items()):
        if locale[k] == module.params[k]:
            continue
        else:
            rc, out, err = module.run_command(['update-locale', '{k}="{v}"'.format(k=k.upper(), v=v)])
            results['changed'] = True

    module.exit_json(**results)


if __name__ == '__main__':
    main()
