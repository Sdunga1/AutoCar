import pytest
import time
from .throttle import ThrottleSystem

def test_throttle_response():
    system = ThrottleSystem()
    response = system.apply_throttle(50.0)
    
    # AC-93: Response within 100ms with accuracy
    assert response['response_time_ms'] <= 100
    assert abs(response['accuracy']) <= 0.1

def test_status_reporting():
    system = ThrottleSystem()
    
    # First status
    status1 = system.get_status()
    time.sleep(0.11)  # Wait just over 100ms
    
    # Second status
    status2 = system.get_status()
    
    # AC-94: Status reported every 100ms
    assert 'position' in status1
    assert 'timestamp' in status1
    assert abs(status2['timestamp'] - status1['timestamp']) >= 0.1
