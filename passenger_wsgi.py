import os
import sys

# Path to project root
project_path = '/home/layeklly/nuit_back'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

# Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()