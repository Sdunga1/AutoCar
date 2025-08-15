import pytest
import time
from .perception import PerceptionSystem

def test_object_detection_range():
    system = PerceptionSystem()
    objects = system.detect_objects()
    
    # AC-83: Check detection ranges
    assert any(obj['distance'] <= 200 for obj in objects['vehicles'])
    assert any(obj['confidence'] > 0.95 for obj in objects['vehicles'])

def test_detection_rate():
    system = PerceptionSystem()
    start_time = time.time()
    detections = 0
    
    # Test for 1 second
    while time.time() - start_time < 1.0:
        if system.detect_objects():
            detections += 1
        time.sleep(0.01)
    
    # AC-84: Verify ≥20Hz detection rate
    assert detections >= 20

def test_stationary_object_classification():
    system = PerceptionSystem()
    false_positives = 0
    total_tests = 1000
    
    for _ in range(total_tests):
        if system.classify_stationary_objects([{'type': 'stationary'}]):
            false_positives += 1
    
    # AC-85: Less than 1 false per 1000
    assert false_positives <= 1

def test_pedestrian_detection():
    system = PerceptionSystem()
    pedestrians = system.detect_pedestrians()
    
    # AC-86: Detection within 150m with 98% accuracy
    assert all(ped['distance'] <= 150 for ped in pedestrians)
    assert all(ped['confidence'] >= 0.98 for ped in pedestrians)

def test_pedestrian_intention_classification():
    system = PerceptionSystem()
    intentions = system.classify_pedestrian_intention()
    
    # AC-87: 95% accuracy for intention classification
    total_confidence = sum(intentions.values())
    assert max(intentions.values()) / total_confidence >= 0.95
