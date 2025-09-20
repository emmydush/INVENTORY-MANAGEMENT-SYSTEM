#!/usr/bin/env python3
"""
Test script to verify internationalization functionality
"""
import os
import sys
import django
from django.conf import settings

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
django.setup()

from django.utils import translation
from django.test import TestCase, Client
from django.urls import reverse

def test_language_switching():
    """Test that language switching works correctly"""
    client = Client()
    
    # Test English
    response = client.get('/en/dashboard/')
    print("English test - Status code:", response.status_code)
    
    # Test French
    response = client.get('/fr/dashboard/')
    print("French test - Status code:", response.status_code)
    
    # Test Kinyarwanda
    response = client.get('/rw/dashboard/')
    print("Kinyarwanda test - Status code:", response.status_code)
    
    print("Language switching tests completed!")

if __name__ == '__main__':
    test_language_switching()