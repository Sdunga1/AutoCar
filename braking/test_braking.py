import pytest
import time
from .braking import BrakingSystem

def test_brake_response_time():
    system = BrakingSystem()
    response = system.apply_brakes(2.0)
    
    # AC-90: Response within 50ms
    assert response['response_time_ms'] <= 50
    assert abs(response['accuracy']) <= 0.2

def test_health_reporting():
    system = BrakingSystem()
    
    # First report
    status1 = system.get_health_status()
    time.sleep(0.11)  # Wait just over 100ms
    
    # Second report
    status2 = system.get_health_status()
    
    # AC-91: Health status reported every 100ms
    assert status1['system_health'] is True
    assert status2['system_health'] is True
