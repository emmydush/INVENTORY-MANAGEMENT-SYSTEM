#!/usr/bin/env python
"""
Test script for inventory alerts system
This script demonstrates how the inventory alerts system works
"""

import os
import sys
import django
from datetime import date, timedelta

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_management.settings')
django.setup()

def test_inventory_alerts():
    """Test the inventory alerts system"""
    print("Testing Inventory Alerts System")
    print("=" * 40)
    
    # Import models
    from ims.models import Product, Category, Supplier, User
    from ims.email_utils import send_low_stock_alert, send_expired_product_alert
    
    # Get or create test data
    try:
        category = Category.objects.first()
        supplier = Supplier.objects.first()
        
        if not category or not supplier:
            print("Error: No categories or suppliers found in database")
            return
            
        # Create or get test products
        low_stock_product, created = Product.objects.get_or_create(
            name='Test Low Stock Item',
            defaults={
                'description': 'Test item for low stock alert',
                'category': category,
                'supplier': supplier,
                'price': 10.00,
                'cost': 5.00,
                'quantity': 2,
                'reorder_level': 10,
            }
        )
        
        expiring_product, created = Product.objects.get_or_create(
            name='Test Expiring Product',
            defaults={
                'description': 'Test item for expiry alert',
                'category': category,
                'supplier': supplier,
                'price': 15.00,
                'cost': 8.00,
                'quantity': 15,
                'reorder_level': 5,
                'expiry_date': date.today() + timedelta(days=3),
            }
        )
        
        print(f"Created/Found test products:")
        print(f"  - {low_stock_product.name}: quantity={low_stock_product.quantity}, reorder_level={low_stock_product.reorder_level}")
        print(f"  - {expiring_product.name}: expiry_date={expiring_product.expiry_date}")
        print()
        
        # Test low stock alert
        print("Testing Low Stock Alert...")
        result = send_low_stock_alert(low_stock_product, low_stock_product.quantity)
        print(f"  Result: {'SUCCESS' if result else 'FAILED'}")
        print()
        
        # Test expired product alert
        print("Testing Expired Product Alert...")
        result = send_expired_product_alert(expiring_product, expiring_product.quantity)
        print(f"  Result: {'SUCCESS' if result else 'FAILED'}")
        print()
        
        # Test management command
        print("Testing Management Command...")
        from ims.management.commands.check_inventory_alerts import Command
        cmd = Command()
        cmd.check_low_stock_products()
        cmd.check_expired_products(7)
        print("  Management command executed successfully")
        print()
        
        print("Test completed successfully!")
        print("Check the console output for email notifications")
        
    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_inventory_alerts()