# Inventory Alerts System

This document explains how the inventory alerts system works and how to configure it.

## Features

1. **Low Stock Alerts**: Automatically sends email notifications when product quantities fall below their reorder levels
2. **Expired Product Alerts**: Sends email notifications for products that have expired or are about to expire
3. **Real-time Notifications**: Alerts are sent immediately when stock levels change
4. **Scheduled Checks**: Regular checks for inventory issues via management commands

## Email Configuration

To enable email notifications, you need to configure the email settings in the System Settings section of the admin panel:

1. Go to Admin Panel → System Settings
2. Fill in the following fields:
   - Email Host (e.g., smtp.gmail.com)
   - Email Port (e.g., 587 for TLS)
   - Email Username (your email address)
   - Email Password (your email password or app-specific password)
   - Email Use TLS (True/False)
   - Email Use SSL (True/False)
   - Email From Address (sender email address)

## How Alerts Work

### Low Stock Alerts
- Triggered automatically when a product's quantity falls below its reorder level
- Sent immediately when stock movements occur (sales or manual adjustments)
- Emails are sent to all admin users with valid email addresses

### Expired Product Alerts
- Checked daily via scheduled tasks
- Sends alerts for products that have already expired
- Sends warnings for products expiring within 7 days

## Management Commands

### check_inventory_alerts
This command checks for both low stock and expired products:

```bash
python manage.py check_inventory_alerts
```

Options:
- `--days-before-expiry N`: Set the number of days before expiry to send warnings (default: 7)

### test_low_stock_alert
Test the low stock alert functionality with a specific product:

```bash
python manage.py test_low_stock_alert <product_id> <quantity>
```

## Setting Up Scheduled Tasks

To run inventory checks automatically, you need to set up scheduled tasks using cron (Linux/Mac) or Task Scheduler (Windows).

### Linux/Mac (cron)
Add this line to your crontab (`crontab -e`) to run checks daily at 9 AM:

```
0 9 * * * /path/to/your/project/manage.py check_inventory_alerts
```

### Windows (Task Scheduler)
1. Open Task Scheduler
2. Create a new task
3. Set trigger to daily at your preferred time
4. Set action to run:
   ```
   python "C:\path\to\your\project\manage.py" check_inventory_alerts
   ```

## Email Templates

The system uses HTML email templates located in `templates/ims/emails/`:

- `low_stock_alert.html`: For low stock notifications
- `expired_product_alert.html`: For expired product notifications
- `notification.html`: For general notifications

You can customize these templates to match your branding.

## Testing Email Configuration

You can test your email configuration using the test command:

```bash
python manage.py test_email_config
```

This will send a test email to verify that your settings are correct.