"""
Setup script for Drift Gym - Autonomous Vehicle Drifting Environment
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="drift-gym",
    version="0.1.0",
    author="Omeed Tehrani",
    author_email="omeed@cs.utexas.edu",
    description="Gymnasium environment for autonomous vehicle drifting research with F1/10 dynamics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/drift-gym-research",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/drift-gym-research/issues",
        "Documentation": "https://github.com/yourusername/drift-gym-research/tree/main/docs",
        "Source Code": "https://github.com/yourusername/drift-gym-research",
    },
    packages=find_packages(include=['drift_gym', 'drift_gym.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Robotics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "gymnasium>=0.29.0",
        "numpy>=1.21.0,<2.0.0",
        "pygame>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "isort>=5.10.0",
        ],
        "rl": [
            "stable-baselines3>=2.0.0",
            "torch>=2.0.0",
        ],
        "vis": [
            "matplotlib>=3.5.0",
            "seaborn>=0.12.0",
        ],
        "all": [
            "stable-baselines3>=2.0.0",
            "torch>=2.0.0",
            "matplotlib>=3.5.0",
            "seaborn>=0.12.0",
            "pandas>=1.3.0",
        ],
    },
    include_package_data=True,
    package_data={
        'drift_gym': ['config/*.yaml', 'scenarios/*.yaml'],
    },
    keywords=[
        "reinforcement-learning",
        "gymnasium",
        "autonomous-vehicles",
        "drifting",
        "robotics",
        "f1tenth",
        "control",
        "simulation",
        "research",
    ],
    entry_points={
        "gymnasium.envs": [
            "AdvancedDriftCar-v0=drift_gym.envs:AdvancedDriftCarEnv",
        ],
    },
)
