import os

import sys

import site

from django.core.wsgi import get_wsgi_application

# Add the app’s directory to the PYTHONPATH

sys.path.append('C:/Users/wagne/Documents/Store/project/')


os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()