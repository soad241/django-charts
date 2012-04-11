from chart_admin import chart_pool



import imp
from django.conf import settings

CHARTS_SOURCE_FILE = 'my_charts'

def autodiscover():
    # Check django/contrib/admin/__init__.py to know what I'm doing :)
    for app in settings.INSTALLED_APPS:
       try:
           app_path = __import__(app, {}, {}, [app.split('.')[-1]]).__path__
       except AttributeError:
           continue

       try:
           imp.find_module(CHARTS_SOURCE_FILE, app_path)
       except ImportError:
           continue

       __import__('%s.%s' % (app, CHARTS_SOURCE_FILE))

