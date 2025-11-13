# 🤖 Supported Robots and Configuration Sources

RobotLib 致力于统一管理来自不同项目和仿真环境的机器人配置。本文件列出了当前库中所有支持的机器人模型及其配置的来源或主要用途。

## 1. trackerLab (运动跟踪与对齐配置)

这些配置主要用于运动模仿（Motion Imitation）或运动跟踪（Motion Tracking）任务，包含关键的关节顺序对齐配置（`align_cfg`）。

### 1.1. 人形机器人 (Humanoids) - Assets

| 机器人模型 | 描述 | 配置源/主要用途 |
| :--- | :--- | :--- |
| **smplx_humanoid** | SMPLX 人体模型配置 | 泛化人形模型，用于模仿学习 |
| **k1** | K1 人形机器人 | 配置源自 K1 平台或相关项目 |
| **r2** | R2 人形机器人 | 配置源自 R2 平台或相关项目 |
| **pi** | Pi 人形机器人 | 配置源自 Pi 平台或相关项目 |
| **pi_plus** | Pi Plus 人形机器人 | 配置源自 Pi Plus 平台或相关项目 |

### 1.2. 四足机器人 (Quadrupeds) - Assets

| 机器人模型 | 描述 | 配置源/主要用途 |
| :--- | :--- | :--- |
| **go2** | Unitree Go2 四足机器人 | 配置源自 Unitree 平台 |
| **unitree** | Unitree 通用配置 | 抽象的 Unitree 四足平台配置 |

### 1.3. 运动对齐配置 (Align Configs)

这些配置确保了 Isaac Lab 和外部（如 Mujoco 或 Tracker）之间的关节/执行器顺序保持一致。

| 配置路径 | 描述 | 目标对齐平台/用途 |
| :--- | :--- | :--- |
| `unitree/g1_29dof_nohand` | Unitree G1 (29自由度，无手) | 用于 TrackerLab 运动对齐 |
| `third_party/r2` | 第三方 R2 机器人配置 | 用于 TrackerLab 运动对齐 |

---

## 2. beyondMimic (高级模仿学习)

这些模块包含用于超越基础模仿学习任务的特定机器人和执行器配置。

| 模块/机器人 | 描述 | 配置源/主要用途 |
| :--- | :--- | :--- |
| **smpl** | SMPL 模型配置 | 高级模仿学习/全身控制 |
| **g1** | Unitree G1 机器人 | 特定于 BeyondMimic 项目的 G1 配置 |
| **actuator** | 执行器通用配置 | 抽象或自定义执行器模型 |

---

## 3. unitree\_rl\_lab (Unitree 强化学习)

这些配置专门用于 Unitree 平台在强化学习环境中的使用。

| 模块/配置 | 描述 | 配置源/主要用途 |
| :--- | :--- | :--- |
| **unitree** | Unitree 机器人配置 | 用于 RL Lab 的 Unitree 基础配置 |
| **unitree\_actuators** | Unitree 执行器配置 | Unitree 平台特有的执行器参数 |

---

## 4. soccerLab (机器人足球仿真)

这些配置用于机器人足球或涉及快速、动态运动的复杂仿真环境。

| 机器人模型 | 描述 | 配置源/主要用途 |
| :--- | :--- | :--- |
| **mosc9** | MOSC9 机器人配置 | 机器人足球仿真平台配置 |

---

## 🔍 其他配置

| 文件/目录 | 描述 |
| :--- | :--- |
| `data/` | 包含外部数据或原始配置的存储位置。 |
| `scripts/` | 包含辅助脚本，例如配置转换或预处理工具。 |