"""
WSGI application module for Render deployment.

This module exists to resolve deployment issues where Render expects a module named 'app.py'.
It simply imports and exposes the WSGI application from the actual inventory_management project.
"""

import os
import sys
from pathlib import Path

# Add the project directory to Python path
# This ensures that the inventory_management module can be found
project_dir = Path(__file__).resolve().parent
if str(project_dir) not in sys.path:
    sys.path.insert(0, str(project_dir))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')

# Import the actual WSGI application
try:
    from inventory_management.wsgi import application
except ImportError as e:
    # Print debugging information
    print(f"Failed to import inventory_management.wsgi: {e}")
    print(f"Python path: {sys.path}")
    print(f"Project directory: {project_dir}")
    print(f"Contents of project directory: {list(project_dir.iterdir()) if project_dir.exists() else 'Directory does not exist'}")
    raise

# Export the application as both 'application' and 'app' to cover different import patterns
app = application
application = application

# Make sure both names are available for import
__all__ = ['app', 'application']