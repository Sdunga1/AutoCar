# AutoCar

An automated car management system for efficient vehicle operations and maintenance.

## System Requirements

### 1. Automated Driving
- Automated Driving System (ADS) engagement and disengagement control
- Continuous subsystem health monitoring
- Lane keeping and pedestrian avoidance capabilities
- Safety-critical timing requirements compliance

### 2. Perception
- Object detection and classification (200m forward, 50m lateral)
- High-frequency object detection (≥20 Hz)
- Pedestrian detection and intention classification
- Backup camera system integration
- Stationary object classification with minimal false positives

### 3. Braking
- Rapid deceleration response (within 50ms)
- Continuous brake health status monitoring
- High-precision deceleration control (±0.2 m/s²)

### 4. Throttle
- Quick acceleration response (within 100ms)
- Continuous throttle position monitoring
- Precise speed control (±0.1 m/s²)

### 5. Human Machine Interface (HMI)
- Clear ADS state indication (visual/audible)
- Continuous system status display
- Error and degradation alerts
- Steering wheel illumination feedback
- Driver intervention request indicators

## Implementation Status
- All major subsystems implemented with test coverage
- Known gaps:
  - Backup Camera System (AC-88)
  - Driver Intervention Indicator (AC-100)

## Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```