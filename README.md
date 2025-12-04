<div align="center">

# 🤖 RobotLib: Universal Asset & Configuration Hub for Isaac Lab

<a href="https://github.com/Renforce-Dynamics/robotlib/stargazers"><img src="https://img.shields.io/github/stars/Renforce-Dynamics/robotlib?style=for-the-badge&color=25c641" alt="GitHub Stars"></a>
<img src="https://img.shields.io/badge/Focus-Humanoid_and_Quadruped_Robotics-informational?style=for-the-badge&logo=siemens&logoColor=white" alt="Focus: Robotics">
<img src="https://img.shields.io/badge/Simulation-Isaac_Lab_&_Mujoco-blueviolet?style=for-the-badge&logo=nvidia&logoColor=white" alt="Isaac Lab Compatible">
<br>
<br>

**A centralized, multi-source configuration manager designed to guarantee seamless robot asset reusability and simulation compatibility across complex robotics domains.**

</div>

---

## ✨ Overview

RobotLib solves the critical challenge of managing heterogeneous robot configurations (URDFs, asset paths, joint limits, control parameters) sourced from various simulation platforms and internal projects. It ensures assets are standardized and instantly usable within the **Isaac Lab** ecosystem.

Our unique value lies in providing the **motion alignment configurations** necessary to bridge the gap between different simulation and control environments, such as aligning Isaac Lab's conventions with those of Mujoco or specific motion trackers.

### 🌟 Core Capabilities

* **Unified Config Management:** Centralizes robot asset definitions from diverse projects (`trackerLab`, `beyondMimic`, `soccerLab`) for easy loading and reusability.
* **Critical Order Alignment (TrackerLab):** Provides pre-configured **motion align configs** crucial for imitation learning and tracking setups. This guarantees that joint and actuator orders (e.g., Isaac Lab vs. Mujoco) are perfectly matched, preventing complex control errors.
* **Rich Asset Library:** Features a curated collection of definitions for state-of-the-art robots and standardized models, including:
    * **Humanoids:** K1, Pi, Pi Plus, R2, and **SMPLX** models.
    * **Quadrupeds:** Unitree Go2.
    * **Unitree Integration:** Dedicated configurations and actuator definitions for Unitree platforms.
* **Simplified Scene Setup:** The central `robotlib.loader` module provides a single entry point for importing all necessary configurations for a new Isaac Lab scene.

---

## 📂 Repository Structure Highlights

The library is organized around the specific robotics domains it supports, ensuring a modular and clean configuration flow:

| Directory | Purpose | Key Content |
| :--- | :--- | :--- |
| `robotlib/loader.py` | **Config Access Point** | The main utility for loading and fetching configurations programmatically. |
| `robotlib/trackerLab/` | **Motion Alignment & Assets** | Contains all the core asset definitions and the crucial **`align_cfg`** sub-module for cross-simulator joint order matching. |
| `robotlib/beyondMimic/` | **Mimic/IL Configurations** | Configurations specifically tailored for motion imitation and learning workflows (e.g., `smpl.py`, `g1.py`). |
| `robotlib/soccerLab/` | **Domain-Specific Configs** | Configurations for complex tasks like robotic soccer (`mosc9.py`). |
| `robotlib/unitree_rl_lab/` | **RL Integration** | Dedicated actuator and robot configs for Unitree platforms in reinforcement learning setups. |
| `docs/robots.md` | **Documentation** | Detailed list and specifications of all supported robot models. |

---

## 🚀 Getting Started

The recommended way to integrate RobotLib into your project is by cloning the repository and installing it in editable mode:

```bash
# Clone the repository
git clone [https://github.com/Renforce-Dynamics/robotlib.git](https://github.com/Renforce-Dynamics/robotlib.git)
cd robotlib

# Install in editable mode
pip install -e .
````

### Configuration Loading

Use the central `loader` module to access configurations, alignment settings, and asset definitions:

```python
# Example: Import the main loader
from robotlib import loader

# Load a specific robot asset definition (e.g., for the K1 humanoid)
k1_asset_cfg = loader.get_asset_config("humanoids/k1") 

# Load the motion alignment configuration for a specific TrackerLab setup
g1_align_cfg = loader.get_align_config("unitree/g1_29dof_nohand")

# Use these configurations to initialize your Isaac Lab environment...
```

-----

## 📚 Compatibility & Supported Models

For a comprehensive list of all robot models, their configuration parameters, and the details on which external sources they are aligned with, please refer to our official documentation:

> 📄 **[Supported Robots Documentation](https://www.google.com/search?q=docs/robots.md)**

-----

## 🤝 Contribution

We welcome external contributions\! If you have suggestions, wish to add support for a new asset configuration, or improve alignment parameters, please feel free to open an issue or submit a pull request.