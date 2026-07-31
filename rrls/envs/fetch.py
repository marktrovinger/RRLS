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

    ARM_DOF_INDICES = {
        "shoulder_pan":    6,
        "shoulder_lift":   7,
        "upperarm_roll":   8,
        "elbow_flex":      9,
        "forearm_roll":   10,
        "wrist_flex":     11,
        "wrist_roll":     12,
    }

    def __init__(
            self,
            shoulder_pan_frictionloss: float | None = None,
            shoulder_pan_damping: float | None = None,
            shoulder_lift_frictionloss: float | None = None,
            shoulder_lift_damping: float | None = None,
            elbow_flex_frictionloss: float | None = None,
            elbow_flex_damping: float | None = None,
            forearm_roll_frictionloss: float | None = None,
            forearm_roll_damping: float | None = None,
            upperarm_roll_frictionloss: float | None = None,
            upperarm_roll_damping: float | None = None,
            wrist_flex_frictionloss: float | None = None,
            wrist_flex_damping: float | None = None,
            wrist_roll_frictionloss: float | None = None,
            wrist_roll_damping: float | None = None,
            **kwargs: dict[str, Any]):
        super().__init__(env = gym.make("FetchReach-v4", **kwargs)) # type: ignore
        self.set_params(
            shoulder_pan_frictionloss =shoulder_pan_frictionloss,
            shoulder_pan_damping = shoulder_pan_damping,
            shoulder_lift_frictionloss = shoulder_lift_frictionloss,
            shoulder_lift_damping = shoulder_lift_damping,
            upperarm_roll_frictionloss = upperarm_roll_frictionloss,
            upperarm_roll_damping = upperarm_roll_damping,
            elbow_flex_frictionloss = elbow_flex_frictionloss,
            elbow_flex_damping = elbow_flex_damping,
            forearm_roll_frictionloss = forearm_roll_frictionloss,
            forearm_roll_damping = forearm_roll_damping,
            wrist_flex_frictionloss = wrist_flex_frictionloss,
            wrist_flex_damping = wrist_flex_damping,
            wrist_roll_frictionloss = wrist_roll_frictionloss,
            wrist_roll_damping = wrist_roll_damping
        )

    def set_params(
            self,
            **kwargs
    ):
        self.shoulder_pan_frictionloss = getattr(kwargs, 
                                                 "shoulder_pan_frictionloss", 
                                                 DEFAULT_PARAMS["shoulder_pan_frictionloss"]) or getattr(kwargs, "shoulder_pan_frictionloss_scale", DEFAULT_PARAMS["shoulder_pan_frictionloss"])
        self.shoulder_pan_damping = getattr(kwargs, 
                                                 "shoulder_pan_damping", 
                                                 DEFAULT_PARAMS["shoulder_pan_damping"]) or getattr(kwargs, "shoulder_pan_damping_scale", DEFAULT_PARAMS["shoulder_pan_damping"])
        self.shoulder_lift_frictionloss = getattr(kwargs, 
                                                 "shoulder_lift_frictionloss", 
                                                 DEFAULT_PARAMS["shoulder_lift_frictionloss"]) or getattr(kwargs, "shoulder_lift_frictionloss_scale", DEFAULT_PARAMS["shoulder_lift_frictionloss"])
        self.shoulder_lift_damping = getattr(kwargs, 
                                                 "shoulder_lift_damping", 
                                                 DEFAULT_PARAMS["shoulder_lift_damping"]) or getattr(kwargs, "shoulder_lift_damping_scale", DEFAULT_PARAMS["shoulder_lift_damping"])
        self.upperarm_roll_frictionloss = getattr(kwargs, 
                                                 "upperarm_roll_frictionloss", 
                                                 DEFAULT_PARAMS["upperarm_roll_frictionloss"]) or getattr(kwargs, "upperarm_roll_frictionloss_scale", DEFAULT_PARAMS["upperarm_roll_frictionloss"])
        self.upperarm_roll_damping = getattr(kwargs, 
                                                 "upperarm_roll_damping", 
                                                 DEFAULT_PARAMS["upperarm_roll_damping"]) or getattr(kwargs, "upperarm_roll_damping_scale", DEFAULT_PARAMS["upperarm_roll_damping"])
        self.elbow_flex_frictionloss = getattr(kwargs, 
                                                 "elbow_flex_frictionloss", 
                                                 DEFAULT_PARAMS["elbow_flex_frictionloss"]) or getattr(kwargs, "elbow_flex_frictionloss_scale", DEFAULT_PARAMS["elbow_flex_frictionloss"])
        self.elbow_flex_damping = getattr(kwargs, 
                                                 "elbow_flex_damping", 
                                                 DEFAULT_PARAMS["elbow_flex_damping"]) or getattr(kwargs, "elbow_flex_damping_scale", DEFAULT_PARAMS["elbow_flex_damping"])
        self.forearm_roll_frictionloss = getattr(kwargs, 
                                                 "forearm_roll_frictionloss", 
                                                 DEFAULT_PARAMS["forearm_roll_frictionloss"]) or getattr(kwargs, "forearm_roll_frictionloss_scale", DEFAULT_PARAMS["forearm_roll_frictionloss"])
        self.forearm_roll_damping = getattr(kwargs, 
                                                 "forearm_roll_damping", 
                                                 DEFAULT_PARAMS["forearm_roll_damping"]) or getattr(kwargs, "forearm_roll_damping_scale", DEFAULT_PARAMS["forearm_roll_damping"])
        self.wrist_flex_frictionloss = getattr(kwargs, 
                                                 "wrist_flex_frictionloss", 
                                                 DEFAULT_PARAMS["wrist_flex_frictionloss"]) or getattr(kwargs, "wrist_flex_frictionloss_scale", DEFAULT_PARAMS["wrist_flex_frictionloss"])
        self.wrist_flex_damping = getattr(kwargs, 
                                                 "wrist_flex_damping", 
                                                 DEFAULT_PARAMS["wrist_flex_damping"]) or getattr(kwargs, "wrist_flex_damping_scale", DEFAULT_PARAMS["wrist_flex_damping"])
        self.wrist_roll_frictionloss = getattr(kwargs, 
                                                 "wrist_roll_frictionloss", 
                                                 DEFAULT_PARAMS["wrist_roll_frictionloss"]) or getattr(kwargs, "wrist_roll_frictionloss_scale", DEFAULT_PARAMS["wrist_roll_frictionloss"])
        self.wrist_roll_damping = getattr(kwargs, 
                                                 "wrist_roll_damping", 
                                                 DEFAULT_PARAMS["wrist_roll_damping"]) or getattr(kwargs, "wrist_roll_damping_scale", DEFAULT_PARAMS["wrist_roll_damping"])
        self._change_params()

    def get_params(self):
        return {
            "shoulder_pan_frictionloss": self.shoulder_pan_frictionloss,
            "shoulder_lift_frictionloss": self.shoulder_lift_frictionloss,
            "upperarm_roll_frictionloss": self.upperarm_roll_frictionloss,
            "elbow_flex_frictionloss": self.elbow_flex_frictionloss,
            "forearm_roll_frictionloss": self.forearm_roll_frictionloss,
            "wrist_flex_frictionloss": self.wrist_flex_frictionloss,
            "wrist_roll_frictionloss": self.wrist_roll_frictionloss,
            "shoulder_pan_damping": self.shoulder_pan_damping,
            "shoulder_lift_damping": self.shoulder_lift_damping,
            "upperarm_roll_damping": self.upperarm_roll_damping,
            "elbow_flex_damping": self.elbow_flex_damping,
            "forearm_roll_damping": self.forearm_roll_damping,
            "wrist_flex_damping": self.wrist_flex_damping,
            "wrist_roll_damping": self.wrist_roll_damping
        }

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        if options is not None:
            self.set_params(**options)
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
                    self.unwrapped.model.dof_armature[idx] = joint[1]
        # if self.shoulder_pan_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["shoulder_pan_joint"]] = self.shoulder_pan_frictionloss  # type: ignore
        # if self.shoulder_pan_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["shoulder_pan_joint"]] = shoulder_pan_damping  # type: ignore
        # if self.shoulder_lift_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["shoulder_lift_joint"]] = shoulder_lift_frictionloss  # type: ignore
        # if self.shoulder_lift_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["shoulder_lift_joint"]] = shoulder_lift_damping  # type: ignore
        # if self.upperarm_roll_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["upperarm_roll_joint"]] = upperarm_roll_frictionloss  # type: ignore
        # if self.upperarm_roll_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["upperarm_roll_joint"]] = upperarm_roll_damping  # type: ignore
        # if self.elbow_flex_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["elbow_flex_joint"]] = elbow_flex_frictionloss  # type: ignore
        # if self.elbow_flex_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["elbow_flex_joint"]] = elbow_flex_damping  # type: ignore
        # if self.forearm_roll_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["forearm_roll_joint"]] = forearm_roll_frictionloss  # type: ignore
        # if self.forearm_roll_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["forearm_roll_joint"]] = forearm_roll_damping  # type: ignore
        # if self.wrist_flex_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["wrist_flex_joint"]] = wrist_flex_frictionloss  # type: ignore
        # if self.wrist_flex_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["wrist_flex_joint"]] = wrist_flex_damping  # type: ignore
        # if self.wrist_roll_frictionloss is not None:
        #     self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["wrist_roll_joint"]] = wrist_roll_frictionloss  # type: ignore
        # if self.wrist_roll_damping is not None:
        #     self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["wrist_roll_joint"]] = wrist_roll_damping  # type: ignore