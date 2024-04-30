import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module for the 'textutil' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

# Create a WSGI application
application = get_wsgi_application()
