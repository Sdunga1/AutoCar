import pytest
import time
from .automated_driving import AutomatedDrivingSystem

def test_engage_success():
    ads = AutomatedDrivingSystem()
    start_time = time.time()
    result = ads.engage()
    end_time = time.time()
    
    assert result is True
    assert ads.is_engaged is True
    assert end_time - start_time < 3.0  # AC-77: Within 3 seconds

def test_disengage_immediate():
    ads = AutomatedDrivingSystem()
    ads.engage()
    
    start_time = time.time()
    ads.disengage()
    end_time = time.time()
    
    assert ads.is_engaged is False
    assert end_time - start_time < 0.2  # AC-78: Within 200ms

def test_health_monitoring():
    ads = AutomatedDrivingSystem()
    ads.engage()
    
    health_status = ads.monitor_health()
    assert all(health_status.values())  # AC-79: All systems healthy

def test_lane_keeping():
    ads = AutomatedDrivingSystem()
    ads.engage()
    
    # AC-80: Stay in lane
    assert ads.handle_lane_keeping(has_pedestrian=False) == "Maintaining lane position"
    
    # AC-81: Leave lane for pedestrian
    assert ads.handle_lane_keeping(has_pedestrian=True) == "Leaving lane to avoid pedestrian"
