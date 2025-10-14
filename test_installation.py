#!/usr/bin/env python3
"""
Quick installation verification script for Drift Gym.
Tests that the standalone environment can be imported and instantiated.
"""

import sys

def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import numpy as np
        print("✓ numpy")
    except ImportError as e:
        print(f"✗ numpy: {e}")
        return False
    
    try:
        import gymnasium as gym
        print("✓ gymnasium")
    except ImportError as e:
        print(f"✗ gymnasium: {e}")
        return False
    
    try:
        import drift_gym
        print(f"✓ drift_gym (version {drift_gym.__version__})")
    except ImportError as e:
        print(f"✗ drift_gym: {e}")
        return False
    
    try:
        from drift_gym.envs import AdvancedDriftCarEnv
        print("✓ AdvancedDriftCarEnv")
    except ImportError as e:
        print(f"✗ AdvancedDriftCarEnv: {e}")
        return False
    
    try:
        from drift_gym.simulator import F110Vehicle, VehicleState
        print("✓ F110Vehicle (standalone)")
    except ImportError as e:
        print(f"✗ F110Vehicle: {e}")
        return False
    
    return True


def test_environment_creation():
    """Test that the environment can be created."""
    print("\nTesting environment creation...")
    
    try:
        import gymnasium as gym
        import drift_gym
        
        # Test with gym.make
        env = gym.make("AdvancedDriftCar-v0", scenario="loose")
        print("✓ Environment created via gym.make")
        
        # Test reset
        obs, info = env.reset(seed=42)
        print(f"✓ Environment reset (obs shape: {obs.shape})")
        
        # Test step
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"✓ Environment step (reward: {reward:.2f})")
        
        env.close()
        return True
        
    except Exception as e:
        print(f"✗ Environment creation failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_standalone_dynamics():
    """Test that vehicle dynamics are standalone."""
    print("\nTesting standalone vehicle dynamics...")
    
    try:
        from drift_gym.envs.drift_car_env_advanced import F110VehicleDynamics, VehicleState
        
        vehicle = F110VehicleDynamics(dt=0.05, enable_slip=True)
        print("✓ F110VehicleDynamics instantiated")
        
        vehicle.reset(x=0.0, y=0.0, theta=0.0)
        print("✓ Vehicle reset")
        
        state = vehicle.step(velocity_cmd=2.0, angular_velocity_cmd=0.5)
        print(f"✓ Vehicle dynamics step (x={state.x:.3f}, y={state.y:.3f})")
        
        return True
        
    except Exception as e:
        print(f"✗ Standalone dynamics test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Drift Gym Installation Verification")
    print("=" * 60)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test environment
    if not test_environment_creation():
        all_passed = False
    
    # Test standalone dynamics
    if not test_standalone_dynamics():
        all_passed = False
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed!")
        print("The environment is fully standalone and ready to use.")
        return 0
    else:
        print("✗ Some tests failed.")
        print("Please check the error messages above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
