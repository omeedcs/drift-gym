#!/usr/bin/env python3
"""
Example usage of the standalone Drift Gym environment.
Demonstrates basic environment interaction and configuration options.
"""

import numpy as np
import gymnasium as gym
import drift_gym


def basic_example():
    """Basic environment usage."""
    print("\n" + "="*60)
    print("Basic Example: Simple Environment Interaction")
    print("="*60)
    
    # Create environment
    env = gym.make("AdvancedDriftCar-v0", scenario="loose")
    
    # Reset
    obs, info = env.reset(seed=42)
    print(f"Initial observation shape: {obs.shape}")
    print(f"Initial position: x={info['x']:.2f}, y={info['y']:.2f}")
    
    # Run a few steps
    total_reward = 0
    for step in range(10):
        # Random action
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        
        if terminated or truncated:
            print(f"Episode ended at step {step}")
            break
    
    print(f"Total reward after 10 steps: {total_reward:.2f}")
    env.close()


def research_config_example():
    """Example with research-grade features enabled."""
    print("\n" + "="*60)
    print("Research Configuration: Full Sensor Suite")
    print("="*60)
    
    # Create environment with all research features
    env = gym.make("AdvancedDriftCar-v0",
                   scenario="tight",              # Challenging scenario
                   use_noisy_sensors=True,        # GPS/IMU noise
                   use_perception_pipeline=True,  # Object detection
                   use_latency=True,              # Realistic delays
                   use_3d_dynamics=True,          # Pitch/roll
                   use_moving_agents=True,        # Traffic
                   max_steps=400,
                   seed=42)
    
    obs, info = env.reset()
    
    print(f"Scenario: {info['scenario']}")
    print(f"Sensor mode: {info['sensor_mode']}")
    print(f"Observation includes:")
    print("  - Goal information (relative position & heading)")
    print("  - EKF state estimates (velocity, angular velocity)")
    print("  - Uncertainties (velocity & angular velocity std)")
    print("  - Obstacle perception")
    print("  - Action history")
    
    # Run episode with simple policy
    episode_reward = 0
    for step in range(400):
        # Simple policy: drive forward, steer toward goal
        # obs[0:2] are relative goal position (normalized)
        steering = np.clip(obs[1] * 2.0, -1.0, 1.0)  # Proportional to lateral offset
        velocity = 0.5  # Constant velocity
        action = np.array([velocity, steering])
        
        obs, reward, terminated, truncated, info = env.step(action)
        episode_reward += reward
        
        if terminated:
            print(f"Episode terminated at step {step}: {info.get('termination_reason', 'unknown')}")
            break
        if truncated:
            print(f"Episode truncated at step {step}")
            break
    
    print(f"Final episode reward: {episode_reward:.2f}")
    env.close()


def baseline_config_example():
    """Example with perfect sensors (baseline comparison)."""
    print("\n" + "="*60)
    print("Baseline Configuration: Perfect Sensors")
    print("="*60)
    
    # Create environment with perfect sensors (for baseline)
    env = gym.make("AdvancedDriftCar-v0",
                   scenario="loose",
                   use_noisy_sensors=False,       # Perfect state
                   use_perception_pipeline=False, # Perfect detection
                   use_latency=False,             # No delays
                   use_3d_dynamics=False,         # 2D only
                   use_moving_agents=False,       # No traffic
                   max_steps=400,
                   seed=42)
    
    obs, info = env.reset()
    
    print(f"Sensor mode: {info['sensor_mode']}")
    print("This configuration provides perfect state information")
    print("Useful for baseline comparisons and initial policy development")
    
    # Run a few steps
    for step in range(10):
        action = np.array([0.7, 0.0])  # Drive forward
        obs, reward, terminated, truncated, info = env.step(action)
        
        if step % 5 == 0:
            print(f"Step {step}: pos=({info['x']:.2f}, {info['y']:.2f}), "
                  f"v={info['velocity']:.2f}, omega={info['angular_velocity']:.2f}")
    
    env.close()


def standalone_dynamics_example():
    """Example of using the standalone vehicle dynamics directly."""
    print("\n" + "="*60)
    print("Standalone Dynamics: Direct Vehicle Control")
    print("="*60)
    
    from drift_gym.envs.drift_car_env_advanced import F110VehicleDynamics, VehicleState
    
    # Create vehicle dynamics
    vehicle = F110VehicleDynamics(dt=0.05, enable_slip=True)
    vehicle.reset(x=0.0, y=0.0, theta=0.0)
    
    print("Simulating drift maneuver...")
    
    # Simulate drift: high speed + sharp turn
    for step in range(50):
        velocity_cmd = 3.0  # High speed
        angular_velocity_cmd = 2.0  # Sharp turn
        
        state = vehicle.step(velocity_cmd, angular_velocity_cmd)
        
        if step % 10 == 0:
            print(f"Step {step}: pos=({state.x:.2f}, {state.y:.2f}), "
                  f"theta={state.theta:.2f}, v={state.velocity:.2f}, "
                  f"omega={state.angular_velocity:.2f}")
    
    print("\nThe vehicle dynamics are fully integrated and standalone!")


def main():
    """Run all examples."""
    print("=" * 60)
    print("Drift Gym Standalone Environment - Usage Examples")
    print("=" * 60)
    
    try:
        basic_example()
        research_config_example()
        baseline_config_example()
        standalone_dynamics_example()
        
        print("\n" + "="*60)
        print("✓ All examples completed successfully!")
        print("="*60)
        print("\nThe environment is fully standalone and ready for:")
        print("  - Reinforcement learning training")
        print("  - Sim-to-real transfer research")
        print("  - Sensor fusion algorithm development")
        print("  - Robust control under uncertainty")
        
    except Exception as e:
        print(f"\n✗ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
