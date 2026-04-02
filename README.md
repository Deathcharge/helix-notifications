# Helix Notifications

A comprehensive, production-ready notification system for the Helix Collective ecosystem. Send notifications across multiple channels with automatic retry logic, rate limiting, and delivery tracking.

## Features

✨ **Multi-Channel Delivery**
- Email notifications
- Webhook notifications
- Discord integration
- Slack integration
- SMS notifications
- Push notifications

🔄 **Reliable Delivery**
- Automatic retry with exponential backoff
- Delivery tracking and status monitoring
- Idempotency support
- Failed notification queue

⚡ **Performance**
- Batch notification sending
- Rate limiting
- Async/await support
- Efficient resource usage

📋 **Developer Friendly**
- Simple, intuitive API
- Template support
- Comprehensive logging
- Type hints throughout

## Installation

```bash
pip install helix-notifications
```

## Quick Start

### Basic Email Notification

```python
from helix_notifications import NotificationService, NotificationPayload, NotificationChannel

# Initialize service
service = NotificationService()

# Create notification
notification = NotificationPayload(
    channel=NotificationChannel.EMAIL,
    recipient="user@example.com",
    subject="Welcome to Helix",
    body="Thank you for joining our platform!"
)

# Send notification
success = await service.send(notification)
```

### Webhook Notification

```python
from helix_notifications import NotificationPayload, NotificationChannel

# Send webhook
webhook = NotificationPayload(
    channel=NotificationChannel.WEBHOOK,
    recipient="https://example.com/webhook",
    subject="Event Notification",
    body="An important event has occurred"
)

await service.send(webhook)
```

### Alert Management

```python
from helix_notifications import AlertSystem, Alert, AlertSeverity

# Initialize alert system
alerts = AlertSystem()

# Create alert
alert = Alert(
    id="alert-001",
    title="High CPU Usage",
    description="CPU usage exceeded 90%",
    severity=AlertSeverity.CRITICAL,
    source="monitoring-system"
)

await alerts.create_alert(alert)

# Get active alerts
critical_alerts = alerts.get_active_alerts(AlertSeverity.CRITICAL)
```

### Batch Notifications

```python
# Send multiple notifications at once
payloads = [
    NotificationPayload(
        channel=NotificationChannel.EMAIL,
        recipient=f"user{i}@example.com",
        subject="Batch Notification",
        body="This is a batch notification"
    )
    for i in range(100)
]

results = await service.send_batch(payloads)
```

## Configuration

```python
config = {
    "email": {
        "provider": "sendgrid",
        "api_key": "your-api-key"
    },
    "webhook": {
        "timeout": 30,
        "max_retries": 3
    },
    "rate_limit": {
        "requests_per_second": 100
    }
}

service = NotificationService(config)
```

## API Reference

### NotificationService

Main service for sending notifications.

**Methods:**
- `send(payload: NotificationPayload) -> bool` - Send single notification
- `send_batch(payloads: List[NotificationPayload]) -> Dict[str, bool]` - Send multiple notifications
- `get_delivery_status(recipient: str) -> Optional[Dict]` - Get delivery status

### EmailService

Handle email notifications.

**Methods:**
- `send(to, subject, body, html, attachments) -> bool` - Send email
- `send_template(to, template_id, context) -> bool` - Send templated email
- `register_template(template_id, template)` - Register email template

### AlertSystem

Manage alerts and alert notifications.

**Methods:**
- `create_alert(alert: Alert) -> str` - Create new alert
- `resolve_alert(alert_id: str)` - Resolve alert
- `get_active_alerts(severity) -> List[Alert]` - Get active alerts

### WebhookRouter

Route webhooks to destinations.

**Methods:**
- `route(event_type, payload) -> bool` - Route webhook
- `register_route(event_type, destination)` - Register webhook route

## Notification Channels

### Email
- Subject and body support
- HTML email support
- File attachments
- Template rendering

### Webhook
- HTTP POST delivery
- Signature verification
- Retry logic
- Delivery tracking

### Discord
- Embed support
- Channel routing
- Mention support
- Rich formatting

### Slack
- Message formatting
- Thread support
- File uploads
- Interactive elements

### SMS
- Character encoding
- Delivery reports
- Long message handling

### Push
- Device targeting
- Badge support
- Custom data
- Deep linking

## Error Handling

```python
try:
    success = await service.send(notification)
    if not success:
        print("Notification failed to send")
except Exception as e:
    print(f"Error sending notification: {e}")
```

## Retry Logic

Notifications automatically retry with exponential backoff:

```python
notification = NotificationPayload(
    channel=NotificationChannel.EMAIL,
    recipient="user@example.com",
    subject="Test",
    body="Test notification",
    max_retries=5  # Retry up to 5 times
)
```

## Rate Limiting

Control notification throughput:

```python
config = {
    "rate_limit": {
        "requests_per_second": 100,
        "burst_size": 200
    }
}

service = NotificationService(config)
```

## Monitoring

Track notification delivery:

```python
# Get delivery status
status = service.get_delivery_status("user@example.com")

# Check failed notifications
failed = service.failed_notifications

# Access delivery log
logs = service.delivery_log
```

## Integration with Helix Ecosystem

helix-notifications integrates seamlessly with other Helix components:

```python
# Use with helix-spirals for workflow notifications
from helix_spirals import WorkflowEngine
from helix_notifications import NotificationService

workflow = WorkflowEngine()
notifications = NotificationService()

# Send notification on workflow completion
await notifications.send(notification)
```

## Best Practices

1. **Use Templates** - Pre-define notification templates for consistency
2. **Batch Operations** - Send multiple notifications in batches for efficiency
3. **Error Handling** - Always handle notification failures gracefully
4. **Rate Limiting** - Respect rate limits to avoid service degradation
5. **Monitoring** - Track delivery status and failed notifications
6. **Testing** - Use mock services for testing

## Performance Considerations

- Batch notifications for better throughput
- Use async/await for non-blocking operations
- Configure appropriate retry limits
- Monitor delivery logs for issues
- Use rate limiting to prevent overload

## Security

- Webhook signatures for verification
- API key management
- Secure credential storage
- Rate limiting to prevent abuse
- Input validation

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for guidelines.

## License

Dual licensed under Apache 2.0 and Proprietary License. See LICENSE and LICENSE.PROPRIETARY for details.

## Support

For issues, questions, or contributions, please visit:
- GitHub: https://github.com/Deathcharge/helix-notifications
- Documentation: https://helix-notifications.readthedocs.io
- Issues: https://github.com/Deathcharge/helix-notifications/issues
