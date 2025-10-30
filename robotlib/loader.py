from typing import Tuple, List, Literal

def load_robot_cfg(robot_type: str)->Tuple[dict, dict]:

    if robot_type == "r2" or robot_type == "r2b":
        from robotlib.trackerLab.assets.humanoids.r2 import R2_CFG
        from robotlib.trackerLab.align_cfg import R2B_MOTION_ALIGN_CFG_GMR
        return R2_CFG, R2B_MOTION_ALIGN_CFG_GMR
    else:
        raise ValueError(f"Unsupported robot type: {robot_type}")