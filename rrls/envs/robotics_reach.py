from __future__ import annotations

from enum import Enum
from typing import Any

import gymnasium as gym
from gymnasium import Wrapper
import gymnasium_robotics 

gym.register_envs(gymnasium_robotics)

DEFAULT_PARAMS = {
    "upperarm_roll_link_mass": 2.3311,
    "forearm_roll_link_mass": 1.6563
}


class ReachParamsBound(Enum):
    SHOULDER_FRICTION = {
        "shoulder_pan_joint": [-0.75, 0.85],
        "shoulder_lift_joint": [-0.75, 0.85],
        "upperarm_roll_joint": [-0.75, 0.85]
    }
    ELBOW_FRICTION = {
        "elbow_flex_joint": [-0.75, 0.85],
        "forearm_roll_joint": [-0.75, 0.85]
    }
    WRIST_FRICTION = {
        "wrist_flex_joint": [-0.75, 0.85],
        "wrist_roll_joint": [-0.75, 0.85],
    }
    WHOLE_ARM_FRICTION = {
        "shoulder_pan_joint": [-0.75, 0.85],
        "shoulder_lift_joint": [-0.75, 0.85],
        "upperarm_roll_joint": [-0.75, 0.85],
        "elbow_flex_joint": [-0.75, 0.85],
        "forearm_roll_joint": [-0.75, 0.85],
        "wrist_flex_joint": [-0.75, 0.85],
        "wrist_roll_joint": [-0.75, 0.85],
    }


class RobustReach(Wrapper):

    metadata = {  # type: ignore
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
    }
    def __init__(
        self,
        **kwargs: dict[str, Any],
    ):
        super().__init__(env = gym.make("FetchReach-v4", **kwargs))
        self.set_params()
    
    def set_params(
            self,
            upperarm_roll_link_mass: float | None = None,
            forearm_roll_link_mass: float | None = None,

    ):
        self.upperarm_roll_link_mass = upperarm_roll_link_mass
        self.forearm_roll_link_mass = forearm_roll_link_mass
        self._change_params(
            upperarm_roll_link_mass=self.upperarm_roll_link_mass,
            forearm_roll_link_mass=self.forearm_roll_link_mass
        )

    def get_params(
            self,
    ):
        return{
            "upperarm_roll_link_mass": self.upperarm_roll_link_mass,
            "forearm_roll_link_mass": self.forearm_roll_link_mass
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
    
    def _change_params(
            self,
            upperarm_roll_link_mass: float | None = None,
            forearm_roll_link_mass: float | None = None,      
    ):
        if self.upperarm_roll_link_mass is not None:
            self.unwrapped.model.body_mass[14] = upperarm_roll_link_mass
        if self.forearm_roll_link_mass is not None:
            self.unwrapped.model.body_mass[16] = forearm_roll_link_mass
    

class RobustReachDense(Wrapper):

    metadata = {  # type: ignore
        "render_modes": [
            "human",
            "rgb_array",
            "depth_array",
        ],
    }
    def __init__(
        self,
        **kwargs: dict[str, Any],
    ):
        super().__init__(env = gym.make("FetchReachDense-v4", **kwargs))
        self.set_params()
    
    def set_params(
            self,
            upperarm_roll_link_mass: float | None = None,
            forearm_roll_link_mass: float | None = None,

    ):
        self.upperarm_roll_link_mass = upperarm_roll_link_mass
        self.forearm_roll_link_mass = forearm_roll_link_mass
        self._change_params(
            upperarm_roll_link_mass=self.upperarm_roll_link_mass,
            forearm_roll_link_mass=self.forearm_roll_link_mass
        )

    def get_params(
            self,
    ):
        return{
            "upperarm_roll_link_mass": self.upperarm_roll_link_mass,
            "forearm_roll_link_mass": self.forearm_roll_link_mass
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
    
    def _change_params(
            self,
            upperarm_roll_link_mass: float | None = None,
            forearm_roll_link_mass: float | None = None,      
    ):
        if self.upperarm_roll_link_mass is not None:
            self.unwrapped.model.body_mass[14] = upperarm_roll_link_mass
        if self.forearm_roll_link_mass is not None:
            self.unwrapped.model.body_mass[16] = forearm_roll_link_mass

class ForceReachDense(Wrapper):
    """
    Force Reach environment. You can apply forces to the robot using the env.data.qfrc_applied
    attribute. This wraps the "dense" reward environment. The parameters are:
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

    def __init__(self,  **kwargs: dict[str, Any]):
        super().__init__(env = gym.make("FetchReachDense-v4", **kwargs))
        self.set_params()
    
    def set_params(
            self,
            shoulder_pan_joint: float | None = None,
            shoulder_lift_joint: float | None = None,
            upperarm_roll_joint: float | None = None,
            elbow_flex_joint: float | None = None,
            forearm_roll_joint: float | None = None,
            wrist_flex_joint: float | None = None,
            wrist_roll_joint: float | None = None,

    ):
        self.shoulder_pan_joint = shoulder_pan_joint
        self.shoulder_lift_joint = shoulder_lift_joint
        self.upperarm_roll_joint = upperarm_roll_joint
        self.elbow_flex_joint = elbow_flex_joint
        self.forearm_roll_joint = forearm_roll_joint
        self.wrist_flex_joint = wrist_flex_joint
        self.wrist_roll_joint = wrist_roll_joint
        self._change_params()

    def get_params(self):
        return{
            "shoulder_pan_joint": self.shoulder_pan_joint,
            "shoulder_lift_joint": self.shoulder_lift_joint,
            "upperarm_roll_joint": self.upperarm_roll_joint,
            "elbow_flex_joint": self.elbow_flex_joint,
            "forearm_roll_joint": self.forearm_roll_joint,
            "wrist_flex_joint": self.wrist_flex_joint,
            "wrist_roll_joint": self.wrist_roll_joint
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
    
    def _change_params(
            self,
            shoulder_pan_joint: float | None = None,
            shoulder_lift_joint: float | None = None,
            upperarm_roll_joint: float | None = None,
            elbow_flex_joint: float | None = None,
            forearm_roll_joint: float | None = None,
            wrist_flex_joint: float | None = None,
            wrist_roll_joint: float | None = None,
    ):
        if self.shoulder_pan_joint is not None:
            self.unwrapped.data.qfrc_applied[6] = shoulder_pan_joint  # type: ignore
        if self.shoulder_lift_joint is not None:
            self.unwrapped.data.qfrc_applied[7] = shoulder_lift_joint  # type: ignore
        if self.upperarm_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[8] = upperarm_roll_joint  # type: ignore
        if self.elbow_flex_joint is not None:
            self.unwrapped.data.qfrc_applied[9] = elbow_flex_joint  # type: ignore
        if self.forearm_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[10] = forearm_roll_joint  # type: ignore
        if self.wrist_flex_joint is not None:
            self.unwrapped.data.qfrc_applied[11] = wrist_flex_joint  # type: ignore
        if self.wrist_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[12] = wrist_roll_joint  # type: ignore

class ForceReach(Wrapper):
    """
    Force Reach environment. You can apply forces to the robot's joints using the env.data.qfrc_applied
    attribute. This wraps the "sparse" reward environment. The parameters are:
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

    def __init__(
            self,
            shoulder_pan_joint: float | None = None,
            shoulder_lift_joint: float | None = None,
            upperarm_roll_joint: float | None = None,
            elbow_flex_joint: float | None = None,
            forearm_roll_joint: float | None = None,
            wrist_flex_joint: float | None = None,
            wrist_roll_joint: float | None = None,
            **kwargs: dict[str, Any]):
        super().__init__(env = gym.make("FetchReach-v4", **kwargs))
        self.set_params()

    def set_params(
            self,
            shoulder_pan_joint: float | None = None,
            shoulder_lift_joint: float | None = None,
            upperarm_roll_joint: float | None = None,
            elbow_flex_joint: float | None = None,
            forearm_roll_joint: float | None = None,
            wrist_flex_joint: float | None = None,
            wrist_roll_joint: float | None = None,

    ):
        self.shoulder_pan_joint = shoulder_pan_joint
        self.shoulder_lift_joint = shoulder_lift_joint
        self.upperarm_roll_joint = upperarm_roll_joint
        self.elbow_flex_joint = elbow_flex_joint
        self.forearm_roll_joint = forearm_roll_joint
        self.wrist_flex_joint = wrist_flex_joint
        self.wrist_roll_joint = wrist_roll_joint
        self._change_params()

    def get_params(self):
        return {
            "shoulder_pan_joint": self.shoulder_pan_joint,
            "shoulder_lift_joint": self.shoulder_lift_joint,
            "upperarm_roll_joint": self.upperarm_roll_joint,
            "elbow_flex_joint": self.elbow_flex_joint,
            "forearm_roll_joint": self.forearm_roll_joint,
            "wrist_flex_joint": self.wrist_flex_joint,
            "wrist_roll_joint": self.wrist_roll_joint
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
    
    def _change_params(
            self,
            shoulder_pan_joint: float | None = None,
            shoulder_lift_joint: float | None = None,
            upperarm_roll_joint: float | None = None,
            elbow_flex_joint: float | None = None,
            forearm_roll_joint: float | None = None,
            wrist_flex_joint: float | None = None,
            wrist_roll_joint: float | None = None,
    ):
        if self.shoulder_pan_joint is not None:
            self.unwrapped.data.qfrc_applied[6] = shoulder_pan_joint  # type: ignore
        if self.shoulder_lift_joint is not None:
            self.unwrapped.data.qfrc_applied[7] = shoulder_lift_joint  # type: ignore
        if self.upperarm_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[8] = upperarm_roll_joint  # type: ignore
        if self.elbow_flex_joint is not None:
            self.unwrapped.data.qfrc_applied[9] = elbow_flex_joint  # type: ignore
        if self.forearm_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[10] = forearm_roll_joint  # type: ignore
        if self.wrist_flex_joint is not None:
            self.unwrapped.data.qfrc_applied[11] = wrist_flex_joint  # type: ignore
        if self.wrist_roll_joint is not None:
            self.unwrapped.data.qfrc_applied[12] = wrist_roll_joint  # type: ignore