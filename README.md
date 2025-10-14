# Drift Gym - Autonomous Vehicle Drifting Environment

A research-grade Gymnasium environment for autonomous vehicle drifting with realistic F1/10 scale vehicle dynamics.

## Features

### **Fully Standalone Environment**
- **Integrated Vehicle Dynamics**: F1/10 vehicle physics with tire slip modeling built directly into the environment
- **No External Dependencies**: Self-contained implementation without reliance on legacy `src.simulator` code
- **Research-Grade Sensors**: GPS drift, IMU bias, and sensor fusion via Extended Kalman Filter
- **Perception Pipeline**: Object detection with configurable false positives/negatives
- **Latency Modeling**: Realistic sensor-compute-actuation delays
- **3D Dynamics**: Optional pitch/roll and weight transfer simulation
- **Moving Agents**: Configurable traffic agents with various behaviors

### **Based on F1/10 Platform**
- UT AUTOmata specifications
- Wheelbase: 0.324m (12.76")
- Vehicle width: 0.48m (19")
- VESC motor controller dynamics
- Vectornav VN-100 IMU characteristics

## Installation

### From Source
```bash
git clone https://github.com/yourusername/drift-gym-research.git
cd drift-gym-research
pip install -e .
```

### With Optional Dependencies
```bash
# For RL training
pip install -e ".[rl]"

# For visualization
pip install -e ".[vis]"

# All extras
pip install -e ".[all]"
```

## Quick Start

```python
import gymnasium as gym
import drift_gym

# Create environment
env = gym.make("AdvancedDriftCar-v0", 
               scenario="loose",
               use_noisy_sensors=True,
               use_perception_pipeline=True)

# Reset environment
obs, info = env.reset()

# Run episode
for _ in range(400):
    action = env.action_space.sample()  # Your policy here
    obs, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        break

env.close()
```

## Environment Configuration

### Scenarios
- **`loose`**: 2.13m gate width (easier drifting)
- **`tight`**: 0.81m gate width (challenging drift maneuver)

### Configuration Flags
```python
env = gym.make("AdvancedDriftCar-v0",
    scenario="loose",              # or "tight"
    use_noisy_sensors=True,        # GPS/IMU noise
    use_perception_pipeline=True,  # Object detection
    use_latency=True,              # Realistic delays
    use_3d_dynamics=True,          # Pitch/roll simulation
    use_moving_agents=True,        # Traffic agents
    max_steps=400,
    seed=42
)
```

## Observation Space

12-dimensional observation vector:
- **Goal information** (3): relative position and heading to gate in body frame
- **State estimates** (2): velocity and angular velocity (from EKF or ground truth)
- **Uncertainties** (2): velocity and angular velocity standard deviations
- **Obstacle perception** (3): count and closest obstacle position
- **Action history** (2): previous velocity and angular velocity commands

## Action Space

2-dimensional continuous control:
- **velocity_cmd**: [-1, 1] → scaled to ±4.0 m/s
- **angular_velocity_cmd**: [-1, 1] → scaled to ±3.0 rad/s

## Reward Structure

- **Distance to gate**: -0.1 × distance
- **Collision penalty**: -50.0
- **Success bonus**: +50.0
- **Clipped**: [-10.0, 10.0]

## Package Structure

```
drift_gym/
├── envs/
│   ├── drift_car_env_advanced.py  # Main environment (standalone)
│   └── __init__.py
├── simulator/
│   ├── vehicle.py                 # F1/10 vehicle dynamics
│   ├── sensors.py                 # IMU, GPS, odometry
│   ├── environment.py             # Simulation environment
│   └── __init__.py
├── sensors/                       # Research-grade sensor models
├── perception/                    # Object detection & tracking
├── dynamics/                      # 3D vehicle dynamics
├── estimation/                    # Extended Kalman Filter
├── agents/                        # Moving agent behaviors
└── __init__.py
```

## Research Applications

This environment is suitable for:
- **Sim-to-real transfer** research with realistic sensor noise
- **Sensor fusion** algorithm development (EKF, UKF, particle filters)
- **Robust control** under uncertainty
- **Multi-agent** planning and coordination
- **Inverse kinodynamics** learning
- **Drift control** via reinforcement learning

## Citation

If you use this environment in your research, please cite:

```bibtex
@software{drift_gym_2024,
  author = {Tehrani, Omeed},
  title = {Drift Gym: A Gymnasium Environment for Autonomous Vehicle Drifting},
  year = {2024},
  url = {https://github.com/yourusername/drift-gym-research}
}
```

## License

MIT License - see LICENSE file for details

## Acknowledgments

Based on the F1/10 autonomous racing platform and inspired by research on inverse kinodynamics learning for drift control.
# drift-gym
