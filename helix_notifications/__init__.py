"""
Helix Notifications Engine

A comprehensive, production-ready notification system supporting multiple channels:
- Email notifications
- Webhook notifications  
- Alert management
- Delivery tracking
- Retry logic
- Rate limiting
"""

__version__ = "1.0.0"
__author__ = "Helix Collective"
__license__ = "Apache 2.0"

from .notification_service import NotificationService
from .email_service import EmailService
from .alert_system import AlertSystem
from .webhook_router import WebhookRouter

__all__ = [
    "NotificationService",
    "EmailService", 
    "AlertSystem",
    "WebhookRouter"
]
