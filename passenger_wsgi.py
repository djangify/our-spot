import os
import sys

# Use the correct Python interpreter path from your .htaccess
INTERP = "/home/sh0wsp0t25/virtualenv/ourspot/3.10/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add the project directory to the path
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, cwd)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'ourspot.settings'

# Create the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()