#!/usr/bin/python
"""
Specific ``wsgi.py`` file for OpenShift integration. It simply activate
a virtualenv and defined ``myblog.wsgi.application``.
"""
import os
import sys
virtenv = os.environ.get('OPENSHIFT_PYTHON_DIR', '.') + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

if 'OPENSHIFT_REPO_DIR' in os.environ:
    repo_dir = os.environ['OPENSHIFT_REPO_DIR']
    config_path = os.path.join(repo_dir, 'extras/myblog.cfg.vagrant')

    # if not os.path.exists(CONFIG_FILE):
    #     template_path = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', '.'),
    #                                  'extras/myblog.cfg.pytemplate')
    #     try:
    #         with open(template_path) as fd:
    #             content = fd.read().format(**os.environ)
    #         with open(CONFIG_FILE, 'w') as fd:
    #             fd.write(content)
    #         os.environ['BLOG_CONFIG_FILE'] = CONFIG_FILE
    #     except:
    #         CONFIG_FILE = './extras/myblog.cfg.example'
    #         os.environ['BLOG_CONFIG_FILE'] = CONFIG_FILE
    #
else:
    config_path = './extras/myblog.cfg.vagrant'

os.environ.setdefault("BLOG_CONFIG_FILE", config_path)
sys.path.append('myblog')
from myblog.wsgi import application
