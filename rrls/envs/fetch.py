from __future__ import annotations

from enum import Enum
from typing import Any

import gymnasium as gym
from gymnasium import Wrapper
import gymnasium_robotics 

FetchParamsBound = {}

DEFAULT_PARAMS = {
    "shoulder_pan_frictionloss": 0.0,
    "shoulder_pan_damping": 50.0,
    "shoulder_pan_armature": 1.0,
    "shoulder_lift_frictionloss": 0.0,
    "shoulder_lift_damping": 50.0,
    "shoulder_lift_armature": 1.0,
    "elbow_flex_frictionloss": 0.0,
    "elbow_flex_damping": 50.0,
    "elbow_flex_armature": 1.0,
    "forearm_roll_frictionloss": 0.0,
    "forearm_roll_damping": 3.5247,
    "forearm_roll_armature": 2.7538,
    "upperarm_roll_frictionloss": 0.0,
    "upperarm_roll_damping": 50.0,
    "upperarm_roll_armature": 1.0,
    "wrist_flex_frictionloss": 0.0,
    "wrist_flex_damping": 50.0,
    "wrist_flex_armature": 1.0,
    "wrist_roll_frictionloss": 0.0,
    "wrist_roll_damping": 50.0,
    "wrist_roll_armature": 1.0
}

class RobustReach(Wrapper):
    """
    Robust Reach environment. You can apply friction, damping and armature moment of intertia changes to the robot's joints using the env.unwrapped.model.dof_frictionloss
    or env.unwrapped.model.dof_damping attributes. This wraps the "sparse" reward environment. The joints that can be perturbed are:
        - shoulder_pan_joint
        - shoulder_lift_joint
        - upperarm_roll_joint
        - elbow_flex_joint
        - forearm_roll_joint
        - wrist_flex_joint
        - wrist_roll_joint
    """
    metadata = {  # type: ignore
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
    }
    _frictionloss = {}
    _damping = {}
    _armature = {}

    # constants for scale calculations
    DELTA_F_MAX = 0.05
    DELTA_D_MAX = 0.25
    DELTA_D_MAX_FOREARM = 1.76
    DELTA_A_MAX = 0.20
    DELTA_A_MAX_FOREARM = 0.55

    ARM_DOF_INDICES = {
        "shoulder_pan":    6,
        "shoulder_lift":   7,
        "upperarm_roll":   8,
        "elbow_flex":      9,
        "forearm_roll":   10,
        "wrist_flex":     11,
        "wrist_roll":     12,
    }
    ARM_JOINTS = [
    "shoulder_pan",
    "shoulder_lift",
    "upperarm_roll",
    "elbow_flex",
    "forearm_roll",
    "wrist_flex",
    "wrist_roll",
    ]

    def __init__(
            self,
            shoulder_pan_frictionloss: float | None = None,
            shoulder_pan_damping: float | None = None,
            shoulder_pan_armature: float | None = None,
            shoulder_lift_frictionloss: float | None = None,
            shoulder_lift_damping: float | None = None,
            shoulder_lift_armature: float | None = None,
            elbow_flex_frictionloss: float | None = None,
            elbow_flex_damping: float | None = None,
            elbow_flex_armature: float | None = None,
            forearm_roll_frictionloss: float | None = None,
            forearm_roll_damping: float | None = None,
            forearm_roll_armature: float | None = None,
            upperarm_roll_frictionloss: float | None = None,
            upperarm_roll_damping: float | None = None,
            upperarm_roll_armature: float | None = None,
            wrist_flex_frictionloss: float | None = None,
            wrist_flex_damping: float | None = None,
            wrist_flex_armature: float | None = None,
            wrist_roll_frictionloss: float | None = None,
            wrist_roll_damping: float | None = None,
            wrist_roll_armature: float | None = None,
            env_id = "FetchReach-v4",
            **kwargs: dict[str, Any]):
        env = gym.make(env_id, **kwargs) # type: ignore
        super().__init__(env=env) # type: ignore
        self.set_params(
            shoulder_pan_frictionloss =shoulder_pan_frictionloss,
            shoulder_pan_damping = shoulder_pan_damping,
            shoulder_pan_armature = shoulder_pan_armature,
            shoulder_lift_frictionloss = shoulder_lift_frictionloss,
            shoulder_lift_damping = shoulder_lift_damping,
            shoulder_lift_armature = shoulder_lift_armature,
            upperarm_roll_frictionloss = upperarm_roll_frictionloss,
            upperarm_roll_damping = upperarm_roll_damping,
            upperarm_roll_armature = upperarm_roll_armature,
            elbow_flex_frictionloss = elbow_flex_frictionloss,
            elbow_flex_damping = elbow_flex_damping,
            elbow_flex_armature = elbow_flex_armature,
            forearm_roll_frictionloss = forearm_roll_frictionloss,
            forearm_roll_damping = forearm_roll_damping,
            forearm_roll_armature = forearm_roll_armature,
            wrist_flex_frictionloss = wrist_flex_frictionloss,
            wrist_flex_damping = wrist_flex_damping,
            wrist_flex_armature = wrist_flex_armature,
            wrist_roll_frictionloss = wrist_roll_frictionloss,
            wrist_roll_damping = wrist_roll_damping,
            wrist_roll_armature = wrist_roll_armature
        )

    def set_params(
            self,
            **kwargs
    ):
        for joint in self.ARM_JOINTS:
            joint_key = f"{joint}_frictionloss"
            if joint_key in kwargs and kwargs[joint_key] is not None:
                self._frictionloss[joint_key] = kwargs[joint_key] 
            elif "frictionloss_scale" in kwargs:
                self._frictionloss[joint_key] = self.DELTA_F_MAX * kwargs["frictionloss_scale"]
            else:
                self._frictionloss[joint_key] = DEFAULT_PARAMS[joint_key]

        for joint in self.ARM_JOINTS:
            joint_key = f"{joint}_damping"
            if joint_key in kwargs and kwargs[joint_key] is not None:
                self._damping[joint_key] = kwargs[joint_key]
            elif "damping_scale" in kwargs:
                if "forearm" not in joint_key:
                    self._damping[joint_key] = self.DELTA_D_MAX * kwargs[joint_key] 
                else:
                    self._damping[joint_key] = self.DELTA_D_MAX_FOREARM * kwargs[joint_key]
            else:
                self._damping[joint_key] = DEFAULT_PARAMS[joint_key]

        for joint in self.ARM_JOINTS:
            joint_key = f"{joint}_armature"
            if joint_key in kwargs and kwargs[joint_key] is not None:
                self._armature[joint_key] = kwargs[joint_key]
            elif "damping_scale" in kwargs:
                if "forearm" not in joint_key:
                    self._armature[joint_key] = self.DELTA_A_MAX * kwargs[joint_key]
                else:
                    self._armature[joint_key] = self.DELTA_A_MAX_FOREARM * kwargs[joint_key]
            else:
                self._armature[joint_key] = DEFAULT_PARAMS[joint_key]

        self._change_params()

    def get_params(self):
        return self._frictionloss | self._damping | self._armature

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        if options is not None:
            self.set_params(**options)
        else:
            # this indicates that we are doing a clean reset
            self.set_params(**DEFAULT_PARAMS)
        obs, info = self.env.reset(seed=seed, options=options)
        info.update(self.get_params())
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        info.update(self.get_params())
        return obs, reward, terminated, truncated, info
    
    def _change_params(self):
        params = self.get_params()
        similar_joints = []
        for idx_key, idx in self.ARM_DOF_INDICES.items():
            similar_joints.clear()
            for param_key, value in params.items():
                if idx_key in param_key:
                    similar_joints.append((param_key, value))
            for joint in similar_joints:
                if "friction" in joint[0]:
                    self.unwrapped.model.dof_frictionloss[idx] = joint[1] # type: ignore
                elif "damping" in joint[0]:
                    self.unwrapped.model.dof_damping[idx] = joint[1] # type: ignore
                else:
                    self.unwrapped.model.dof_armature[idx] = joint[1] # type: ignore