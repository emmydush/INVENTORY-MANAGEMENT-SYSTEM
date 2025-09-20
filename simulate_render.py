#!/usr/bin/env python3
"""
Simulate what Render might be doing during deployment.
"""

import sys
import os
from pathlib import Path

def simulate_render_import():
    """Simulate Render's import process."""
    print("=== SIMULATING RENDER IMPORT PROCESS ===")
    
    # Set up environment like Render would
    os.environ['DJANGO_SETTINGS_MODULE'] = 'inventory_management.settings'
    
    # Add project directory to path
    project_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(project_dir))
    
    print(f"Project directory: {project_dir}")
    print(f"Python path: {sys.path[:5]}...")
    
    # Try the import that Render might be attempting
    import_tests = [
        "import app",
        "from app import application",
        "import inventory_management.wsgi",
        "from inventory_management.wsgi import application",
    ]
    
    for test in import_tests:
        print(f"\nTesting: {test}")
        try:
            exec(test)
            print(f"  ✓ SUCCESS")
        except Exception as e:
            print(f"  ✗ FAILED: {e}")
            print(f"    Error type: {type(e).__name__}")

if __name__ == "__main__":
    simulate_render_import()