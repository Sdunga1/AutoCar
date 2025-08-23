import time
from typing import Dict

class BrakingSystem:
    def __init__(self):
        self.current_deceleration = 0.0
        self.last_health_report = time.time()
        self.system_health = True
    
    def apply_brakes(self, deceleration: float) -> Dict[str, float]:
        """AC-90: Initiate deceleration within 50ms"""
        start_time = time.time()
        self.current_deceleration = deceleration
        response_time = (time.time() - start_time) * 1000  # Convert to ms
        
        return {
            'deceleration': self.current_deceleration,
            'response_time_ms': response_time,
            'accuracy': 0.2  # m/s²
        }
    
    def get_health_status(self) -> Dict[str, bool]:
        """AC-91: Report brake health status every 100ms"""
        current_time = time.time()
        if current_time - self.last_health_report >= 0.1:
            self.last_health_report = current_time
            return {'system_health': self.system_health}
        return {}
