import pytest
import time
from .hmi import HMISystem

def test_ads_state_notification():
    system = HMISystem()
    response = system.notify_ads_state_change(True)
    
    # AC-96: Notification within 200ms
    assert response['response_time_ms'] <= 200
    assert response['notification'] == "ADS Engaged"

def test_continuous_status_display():
    system = HMISystem()
    system.notify_ads_state_change(True)
    status = system.get_ads_status_display()
    
    # AC-97: Status display with 99% readability
    assert status['status'] == 'Active'
    assert status['readability'] >= 0.99

def test_error_alert():
    system = HMISystem()
    response = system.alert_system_error("Perception Degraded")
    
    # AC-98: Alert within 500ms with guidance
    assert response['response_time_ms'] <= 500
    assert response['guidance_provided'] is True

def test_steering_wheel_indication():
    system = HMISystem()
    response = system.set_steering_wheel_indication(True)
    
    # AC-99: Green indication within 200ms
    assert response['response_time_ms'] <= 200
    assert response['color'] == 'green'
