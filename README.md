Retropie
=========
[![Galaxy](https://img.shields.io/badge/galaxy-samdoran.retropie-blue.svg?style=flat)](https://galaxy.ansible.com/samdoran/retropie)
[![Build Status](https://travis-ci.org/samdoran/ansible-role-retropie.svg?branch=master)](https://travis-ci.org/samdoran/ansible-role-retropie)

Setup [RetroPie](https://retropie.org.uk) to turn a Pi into a retro gaming station.

This role clones the RetroPie repo. After this role runs, you will need to run `/home/{{ retropie_user }}/RetroPie/retropie_setup.sh` to install and configure RetroPie.

Requirements
------------

None.

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `retropie_user` | `retropie` | User account where RetroPie will be cloned and that will run RetroPie. |
| `retropie_group` | `retropie` | Group for `retropie_user` |
| `retropie_extra_groups` | `[sudo]` | Extra groups `{{ retropie_user }}` will be added to. |
| `retropie_git_repo` | `https://github.com/RetroPie/RetroPie-Setup.git` | URL to download RetroPie from. |
| `retropie_version` | `HEAD` | Version to checkout |


Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
         - samdoran.retropie

License
-------

Apache 2.0
