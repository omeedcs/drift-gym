# Quick Start Guide - Standalone Drift Gym

## ✅ Refactoring Complete!

The `drift_car_env_advanced.py` environment is now **fully standalone** with integrated vehicle dynamics. No dependency on `src.simulator` code.

## Installation

```bash
cd /Users/omeedtehrani/drift-gym-research

# Install in development mode
pip install -e .

# Or with all extras
pip install -e ".[all]"
```

## Verify Installation

```bash
python test_installation.py
```

Expected output:
```
✓ numpy
✓ gymnasium
✓ drift_gym (version 0.1.0)
✓ AdvancedDriftCarEnv
✓ F110Vehicle (standalone)
✓ Environment created via gym.make
✓ Environment reset
✓ Environment step
✓ All tests passed!
```

## Basic Usage

```python
import gymnasium as gym
import drift_gym

# Create environment
env = gym.make("AdvancedDriftCar-v0", scenario="loose")

# Reset
obs, info = env.reset(seed=42)

# Run episode
for _ in range(400):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        break

env.close()
```

## Run Examples

```bash
python example_usage.py
```

This will demonstrate:
- Basic environment interaction
- Research configuration (with sensors, perception, etc.)
- Baseline configuration (perfect sensors)
- Standalone dynamics usage

## Key Features

### 🔧 **Standalone Vehicle Dynamics**
- F1/10 physics integrated directly in the environment
- No external simulator dependencies
- Direct velocity + angular velocity control

### 🎯 **Research-Grade Features**
- Noisy sensors (GPS, IMU)
- Sensor fusion (Extended Kalman Filter)
- Object detection & tracking
- Latency modeling
- 3D dynamics (optional)
- Moving agents (optional)

### 📦 **Proper Packaging**
- Modern `pyproject.toml` configuration
- Gymnasium registration
- Comprehensive documentation
- Example scripts

## What Was Changed?

### ✅ Created/Modified Files:
1. **`drift_gym/envs/drift_car_env_advanced.py`**
   - Added `F110VehicleDynamics` class (integrated)
   - Added `VehicleState` and `Obstacle` dataclasses
   - Removed dependency on `src.simulator.environment`

2. **`drift_gym/simulator/environment.py`**
   - Fixed imports: `src.simulator` → `drift_gym.simulator`

3. **`drift_gym/simulator/__init__.py`** (new)
   - Exposes simulator classes

4. **Root package files** (all new):
   - `setup.py` - Package configuration
   - `pyproject.toml` - Modern Python packaging
   - `requirements.txt` - Dependencies
   - `MANIFEST.in` - Package data
   - `README.md` - Documentation
   - `LICENSE` - MIT License
   - `.gitignore` - Python gitignore
   - `test_installation.py` - Verification script
   - `example_usage.py` - Usage examples

## Next Steps

1. **Test it out**:
   ```bash
   python test_installation.py
   python example_usage.py
   ```

2. **Train an agent**:
   ```python
   from stable_baselines3 import PPO
   import gymnasium as gym
   import drift_gym
   
   env = gym.make("AdvancedDriftCar-v0")
   model = PPO("MlpPolicy", env, verbose=1)
   model.learn(total_timesteps=100_000)
   ```

3. **Run your experiments**:
   - The environment works with your existing experiment scripts
   - Just ensure they import `drift_gym` before creating the environment

## Troubleshooting

### Import Errors
If you get import errors, make sure you've installed the package:
```bash
pip install -e .
```

### Missing Dependencies
Install all dependencies:
```bash
pip install -r requirements.txt
```

### Still Using Old Code?
Make sure you're not importing from `src.simulator`:
```bash
# This should return no results
grep -r "from src.simulator" drift_gym/
```

## Architecture

```
AdvancedDriftCarEnv (Fully Standalone)
├── F110VehicleDynamics (integrated)
│   ├── Vehicle physics
│   ├── Tire slip modeling
│   └── Direct control interface
├── VehicleState (integrated)
├── Obstacle (integrated)
└── Optional research modules
    ├── GPSSensor
    ├── IMUSensor
    ├── ExtendedKalmanFilter
    ├── ObjectDetector
    └── MovingAgentSimulator
```

## Success! 🎉

Your environment is now fully standalone and ready for:
- ✅ Reinforcement learning training
- ✅ Sim-to-real transfer research
- ✅ Sensor fusion development
- ✅ Robust control under uncertainty
- ✅ Distribution via PyPI (if desired)

For more details, see `REFACTORING_SUMMARY.md`.
