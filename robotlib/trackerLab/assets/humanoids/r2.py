import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

from robotlib import ROBOTLIB_USD_DIR, ROBOTLIB_ASSETLIB_DIR

STIFFNESS_100 = 100.0
STIFFNESS_150 = 150.0
STIFFNESS_30 = 30.0
STIFFNESS_300 = 300.0
STIFFNESS_50 = 50.0

NATURAL_FREQ = 10 * 2.0 * 3.1415926535  # 10Hz

# ARMATURE_100 = STIFFNESS_100 / NATURAL_FREQ**2
# ARMATURE_150 = STIFFNESS_150 / NATURAL_FREQ**2
# ARMATURE_30 = STIFFNESS_30 / NATURAL_FREQ**2
# ARMATURE_300 = STIFFNESS_300 / NATURAL_FREQ**2
# ARMATURE_50 = STIFFNESS_50 / NATURAL_FREQ**2
ARMATURE_100 = 0.01
ARMATURE_150 = 0.01
ARMATURE_30 = 0.01
ARMATURE_300 = 0.01 
ARMATURE_50 = 0.01


JOINT_NAMES = [
    "left_hip_pitch_joint", #<limit lower="-2.530727415" upper="2.879793266" effort="130" velocity="14.658" />
    "left_hip_roll_joint", #<limit lower="-0.2618" upper="2.4435" effort="130" velocity="14.658" />
    "left_hip_yaw_joint", #<limit lower="-2.7576" upper="2.7576" effort="90" velocity="16.438" />
    "left_knee_joint", #<limit lower="-0.401425728" upper="2.42600766" effort="150" velocity="14.658" />
    "left_ankle_pitch_joint", #<limit lower="-0.69813" upper="0.5236" effort="75" velocity="12.25" />
    "left_ankle_roll_joint", #<limit lower="-0.2618" upper="0.2618" effort="75" velocity="12.25" />
    "right_hip_pitch_joint", #  <limit lower="-2.530727415" upper="2.879793266" effort="130" velocity="14.658" />
    "right_hip_roll_joint", # <limit lower="-2.4435" upper="0.2618" effort="130" velocity="14.658" />
    "right_hip_yaw_joint", #  <limit lower="-2.7576" upper="2.7576" effort="90" velocity="16.438" />
    "right_knee_joint", #  <limit lower="-0.401425728" upper="2.42600766" effort="150" velocity="14.658" />
    "right_ankle_pitch_joint", #  <limit lower="-0.69813" upper="0.5236" effort="75" velocity="12.25" />
    "right_ankle_roll_joint", #  <limit lower="-0.2618" upper="0.2618" effort="75" velocity="12.25" />
    "waist_yaw_joint", #  <limit lower="-0.5236" upper="0.5236" effort="90" velocity="16.438" />
    "waist_pitch_joint", #  <limit lower="-0.5236" upper="0.5236" effort="90" velocity="16.438" />
    "left_shoulder_pitch_joint", #  <limit lower="-3.0892" upper="2.6704" effort="36" velocity="17.904" />
    "left_shoulder_roll_joint", #   <limit lower="-0.5236" upper="2.2427" effort="36" velocity="17.904" />
    "left_shoulder_yaw_joint", #  <limit lower="-2.618" upper="2.618" effort="36" velocity="17.904" />
    "left_arm_pitch_joint", # <limit lower="-1.0472" upper="2.0944" effort="36" velocity="17.904" />
    "right_shoulder_pitch_joint", # <limit lower="-3.0892" upper="2.6704" effort="36" velocity="17.904" />
    "right_shoulder_roll_joint", #  <limit lower="-2.2427" upper="0.5236" effort="36" velocity="17.904" />
    "right_shoulder_yaw_joint", #  <limit lower="-2.618" upper="2.618" effort="36" velocity="17.904" />
    "right_arm_pitch_joint", #  <limit lower="-1.0472" upper="2.0944" effort="36" velocity="17.904" />
]

INIT_POS={
    # left leg
    "left_hip_pitch_joint": -0.1,
    "left_hip_roll_joint": 0.0,
    "left_hip_yaw_joint": 0.0,
    "left_knee_joint": 0.3,
    "left_ankle_pitch_joint": -0.2,
    "left_ankle_roll_joint": 0.0,
    # right leg
    "right_hip_pitch_joint": -0.1,
    "right_hip_roll_joint": 0.0,
    "right_hip_yaw_joint": 0.0,
    "right_knee_joint": 0.3,
    "right_ankle_pitch_joint": -0.2,
    "right_ankle_roll_joint": 0.0,
    # waist
    "waist_yaw_joint": 0.0,
    "waist_pitch_joint": 0.0,
    # arms
    "left_shoulder_pitch_joint": 0.0,
    "left_shoulder_roll_joint": 0.0,
    "left_shoulder_yaw_joint": 0.0,
    "left_arm_pitch_joint": 0.0,
    "right_shoulder_pitch_joint": 0.0,
    "right_shoulder_roll_joint": 0.0,
    "right_shoulder_yaw_joint": 0.0,
    "right_arm_pitch_joint": 0.0,
}

STIFFNESS_REAL={
    # left leg
    "left_hip_pitch_joint": 100.0,
    "left_hip_roll_joint": 100.0,
    "left_hip_yaw_joint": 100.0,
    "left_knee_joint": 150.0,
    "left_ankle_pitch_joint": 30.0,
    "left_ankle_roll_joint": 30.0,
    # right leg
    "right_hip_pitch_joint": 100.0,
    "right_hip_roll_joint": 100.0,
    "right_hip_yaw_joint": 100.0,
    "right_knee_joint": 150.0,
    "right_ankle_pitch_joint": 30.0,
    "right_ankle_roll_joint": 30.0,
    # waist
    "waist_yaw_joint": 300.0,
    "waist_pitch_joint": 300.0,
    # arms
    "left_shoulder_pitch_joint": 100.0,
    "left_shoulder_roll_joint": 100.0,
    "left_shoulder_yaw_joint": 50.0,
    "left_arm_pitch_joint": 50.0,
    "right_shoulder_pitch_joint": 100.0,
    "right_shoulder_roll_joint": 100.0,
    "right_shoulder_yaw_joint": 50.0,
    "right_arm_pitch_joint": 50.0,
}

DAMPING_REAL={
    # left leg
    "left_hip_pitch_joint": 5.0,
    "left_hip_roll_joint": 5.0,
    "left_hip_yaw_joint": 5.0,
    "left_knee_joint": 7.0,
    "left_ankle_pitch_joint": 3.0,
    "left_ankle_roll_joint": 3.0,
    # right leg
    "right_hip_pitch_joint": 5.0,
    "right_hip_roll_joint": 5.0,
    "right_hip_yaw_joint": 5.0,
    "right_knee_joint": 7.0,
    "right_ankle_pitch_joint": 3.0,
    "right_ankle_roll_joint": 3.0,
    # waist
    "waist_yaw_joint": 3.0,
    "waist_pitch_joint": 3.0,
    # arms
    "left_shoulder_pitch_joint": 2.0,
    "left_shoulder_roll_joint": 2.0,
    "left_shoulder_yaw_joint": 2.0,
    "left_arm_pitch_joint": 2.0,
    "right_shoulder_pitch_joint": 2.0,
    "right_shoulder_roll_joint": 2.0,
    "right_shoulder_yaw_joint": 2.0,
    "right_arm_pitch_joint": 2.0,
}

EFFORT_REAL={
    # left leg
    "left_hip_pitch_joint": 130.0,
    "left_hip_roll_joint": 130.0,
    "left_hip_yaw_joint": 90.0,
    "left_knee_joint": 150.0,
    "left_ankle_pitch_joint": 75.0,
    "left_ankle_roll_joint": 75.0,
    # right leg
    "right_hip_pitch_joint": 130.0,
    "right_hip_roll_joint": 130.0,
    "right_hip_yaw_joint": 90.0,
    "right_knee_joint": 150.0,
    "right_ankle_pitch_joint": 75.0,
    "right_ankle_roll_joint": 75.0,
    # waist
    "waist_yaw_joint": 90.0,
    "waist_pitch_joint": 90.0,
    # arms
    "left_shoulder_pitch_joint": 36.0,
    "left_shoulder_roll_joint": 36.0,
    "left_shoulder_yaw_joint": 36.0,
    "left_arm_pitch_joint": 36.0,
    "right_shoulder_pitch_joint": 36.0,
    "right_shoulder_roll_joint": 36.0,
    "right_shoulder_yaw_joint": 36.0,
    "right_arm_pitch_joint": 36.0,
}

R2_ACTION_SCALE={
    # left leg
    "left_hip_pitch_joint": 2.879793266,
    "left_hip_roll_joint": 2.4435,
    "left_hip_yaw_joint": 2.7576,
    "left_knee_joint": 2.42600766,
    "left_ankle_pitch_joint": 0.69813,
    "left_ankle_roll_joint": 0.2618,
    # right leg
    "right_hip_pitch_joint": 2.879793266,
    "right_hip_roll_joint": 2.4435,
    "right_hip_yaw_joint": 2.7576,
    "right_knee_joint": 2.42600766,
    "right_ankle_pitch_joint": 0.69813,
    "right_ankle_roll_joint": 0.2618,
    # waist
    "waist_yaw_joint": 0.5236,
    "waist_pitch_joint": 0.5236,
    # arms
    "left_shoulder_pitch_joint": 3.0892,
    "left_shoulder_roll_joint": 2.2427,
    "left_shoulder_yaw_joint": 2.618,
    "left_arm_pitch_joint": 2.0944,
    "right_shoulder_pitch_joint": 3.0892,
    "right_shoulder_roll_joint": 2.2427,
    "right_shoulder_yaw_joint": 2.618,
    "right_arm_pitch_joint": 2.0944,
}

R2_ARMATURE = \
{
    # left leg
    "left_hip_pitch_joint": ARMATURE_100,
    "left_hip_roll_joint": ARMATURE_100,
    "left_hip_yaw_joint": ARMATURE_100,
    "left_knee_joint": ARMATURE_150,
    "left_ankle_pitch_joint": ARMATURE_30,
    "left_ankle_roll_joint": ARMATURE_30,
    # right leg
    "right_hip_pitch_joint": ARMATURE_100,
    "right_hip_roll_joint": ARMATURE_100,
    "right_hip_yaw_joint": ARMATURE_100,
    "right_knee_joint": ARMATURE_150,
    "right_ankle_pitch_joint": ARMATURE_30,
    "right_ankle_roll_joint": ARMATURE_30,
    # waist
    "waist_yaw_joint": ARMATURE_300,
    "waist_pitch_joint": ARMATURE_300,
    # arms
    "left_shoulder_pitch_joint": ARMATURE_100,
    "left_shoulder_roll_joint": ARMATURE_100,
    "left_shoulder_yaw_joint": ARMATURE_50,
    "left_arm_pitch_joint": ARMATURE_50,
    "right_shoulder_pitch_joint": ARMATURE_100,
    "right_shoulder_roll_joint": ARMATURE_100,
    "right_shoulder_yaw_joint": ARMATURE_50,
    "right_arm_pitch_joint": ARMATURE_50,
}

##
# Configuration
##

R2_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ROBOTLIB_ASSETLIB_DIR}/thrid_party/r2_wholebody/usd/r2_wb.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            fix_root_link=False,
            enabled_self_collisions=False, 
            solver_position_iteration_count=4, 
            solver_velocity_iteration_count=4
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.665),
        joint_pos=INIT_POS,
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=1.0,
    actuators={
        "actuators": ImplicitActuatorCfg(
            joint_names_expr=list(EFFORT_REAL.keys()),
            stiffness=STIFFNESS_REAL,
            damping=DAMPING_REAL,
            effort_limit=EFFORT_REAL,
            armature=R2_ARMATURE
        )
    }
)

"""Configuration for the R2 Humanoid Robot."""
