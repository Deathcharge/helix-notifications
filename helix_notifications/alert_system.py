"""
Alert System

Manages alerts and alert notifications with severity levels,
escalation policies, and delivery rules.
"""

from enum import Enum
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


class AlertSeverity(str, Enum):
    """Alert severity levels"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class Alert:
    """Alert structure"""
    id: str
    title: str
    description: str
    severity: AlertSeverity
    source: str
    metadata: Optional[Dict[str, Any]] = None


class AlertSystem:
    """Alert management system"""
    
    def __init__(self):
        """Initialize alert system"""
        self.alerts: Dict[str, Alert] = {}
        self.escalation_policies: Dict[str, List[str]] = {}
        
    async def create_alert(self, alert: Alert) -> str:
        """Create new alert"""
        self.alerts[alert.id] = alert
        logger.info(f"Alert created: {alert.id} ({alert.severity})")
        return alert.id
    
    async def resolve_alert(self, alert_id: str):
        """Resolve alert"""
        if alert_id in self.alerts:
            del self.alerts[alert_id]
            logger.info(f"Alert resolved: {alert_id}")
    
    def get_active_alerts(self, severity: Optional[AlertSeverity] = None) -> List[Alert]:
        """Get active alerts, optionally filtered by severity"""
        alerts = list(self.alerts.values())
        if severity:
            alerts = [a for a in alerts if a.severity == severity]
        return alerts
