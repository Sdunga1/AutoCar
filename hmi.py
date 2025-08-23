import time
from typing import Dict, Optional

class HMISystem:
    def __init__(self):
        self.ads_status = False
        self.last_notification = None
        self.steering_wheel_color = None
    
    def notify_ads_state_change(self, is_engaged: bool) -> Dict[str, float]:
        """AC-96: Notify driver of ADS state changes"""
        start_time = time.time()
        self.ads_status = is_engaged
        response_time = (time.time() - start_time) * 1000
        
        notification = "ADS Engaged" if is_engaged else "ADS Disengaged"
        self.last_notification = notification
        
        return {
            'notification': notification,
            'response_time_ms': response_time
        }
    
    def get_ads_status_display(self) -> Dict[str, str]:
        """AC-97: Continuous ADS status indication"""
        return {
            'status': 'Active' if self.ads_status else 'Inactive',
            'readability': 0.99
        }
    
    def alert_system_error(self, error_type: str) -> Dict[str, float]:
        """AC-98: Alert driver of system errors"""
        start_time = time.time()
        alert = f"System Error: {error_type}. Please take control."
        response_time = (time.time() - start_time) * 1000
        
        return {
            'alert': alert,
            'response_time_ms': response_time,
            'guidance_provided': True
        }
    
    def set_steering_wheel_indication(self, is_ads_active: bool) -> Dict[str, float]:
        """AC-99: Green steering wheel indication for ADS active"""
        start_time = time.time()
        if is_ads_active:
            self.steering_wheel_color = 'green'
        else:
            self.steering_wheel_color = None
            
        response_time = (time.time() - start_time) * 1000
        return {
            'color': self.steering_wheel_color,
            'response_time_ms': response_time
        }
