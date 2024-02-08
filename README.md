------------------------
ckanext-p30skin_theme
based on ckanext-ozwillo-theme
------------------------

Requirements
============

This extension is compatible with CKAN 2.9 and higher.


Config Settings
===============

The following configuration variables must be set:

* `ckanext.p30skin_theme.plugin.p30skin_url` 
* `ckanext.p30skin_theme.plugin.p30skin_portal_url` 
* `ckanext.p30skin_theme.plugin.p30skin_ckan_app_id` (CKAN app UUID in p30skin portal)


Development Installation
========================

To install ckanext-p30skin_theme for development, activate your CKAN
virtualenv and do:

    git clone https://github.com/rarsenal/ckanext-p30skin_theme.git
    cd ckanext-p30skin_theme
    python setup.py develop
    pip install -r dev-requirements.txt
