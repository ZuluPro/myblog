"""
Production settings for myblog project.
"""
from .common import *
from .env import CONFIG

SECRET_KEY = CONFIG.get('DEFAULT', 'secret_key')
