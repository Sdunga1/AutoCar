import time
from typing import Dict, List, Optional

class AutomatedDrivingSystem:
    def __init__(self):
        self.is_engaged = False
        self.subsystems_health = {
            'perception': True,
            'braking': True,
            'throttle': True
        }
        self.last_health_check = time.time()
    
    def engage(self) -> bool:
        """AC-77: Engage ADS within 3 seconds if safety conditions met"""
        if all(self.subsystems_health.values()):
            time.sleep(0.5)  # Simulating system checks
            self.is_engaged = True
            return True
        return False
    
    def disengage(self) -> None:
        """AC-78: Disengage immediately on manual intervention"""
        self.is_engaged = False
    
    def monitor_health(self) -> Dict[str, bool]:
        """AC-79: Monitor subsystem health continuously"""
        current_time = time.time()
        if current_time - self.last_health_check >= 0.5:  # Check every 500ms
            self.last_health_check = current_time
            return self.subsystems_health
        return {}
    
    def handle_lane_keeping(self, has_pedestrian: bool) -> str:
        """AC-80, AC-81: Lane keeping and pedestrian avoidance"""
        if not self.is_engaged:
            return "ADS not engaged"
        
        if has_pedestrian:
            return "Leaving lane to avoid pedestrian"
        return "Maintaining lane position"
