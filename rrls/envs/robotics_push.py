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

class RobustPush(Wrapper):

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
        super().__init__(env = gym.make("FetchPush-v4", **kwargs))
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
    

class RobustPushDense(Wrapper):

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
        super().__init__(env = gym.make("FetchPushDense-v4", **kwargs))
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

class ForcePushDense(Wrapper):
    """
    Force Push environment. You can apply forces to the robot using the env.data.qfrc_applied
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
        super().__init__(env = gym.make("FetchPushDense-v4", **kwargs))
        self.set_params()

    def set_params(
            self,
            upperarm_x: float | None = None,
            upperarm_y: float | None = None,
            upperarm_z: float | None = None,
            shoulder_lift_link_x: float | None = None,
            shoulder_lift_link_y: float | None = None,
            shoulder_lift_link_z: float | None = None,
    ):
        self.upperarm_x = upperarm_x
        self.upperarm_y = upperarm_y
        self.upperarm_z = upperarm_z
        self.shoulder_lift_link_x = shoulder_lift_link_x
        self.shoulder_lift_link_y = shoulder_lift_link_y
        self.shoulder_lift_link_z = shoulder_lift_link_z
        self._change_params()

    def get_params(self):
        return{
            "upperarm_x": self.upperarm_x,
            "upperarm_y": self.upperarm_y,
            "upperarm_z": self.upperarm_z,
            "shoulder_lift_link_x": self.shoulder_lift_link_x,
            "shoulder_lift_link_y": self.shoulder_lift_link_y,
            "shoulder_lift_link_z": self.shoulder_lift_link_z
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
            upperarm_x: float | None = None,
            upperarm_y: float | None = None,
            upperarm_z: float | None = None,
            shoulder_lift_link_x: float | None = None,
            shoulder_lift_link_y: float | None = None,
            shoulder_lift_link_z: float | None = None,
    ):
        if self.upperarm_x is not None:
            self.unwrapped.data.xfrc_applied[1, 0] = self.upperarm_x  # type: ignore
        if self.shoulder_lift_link_z is not None:
            self.unwrapped.data.xfrc_applied[13, 2] = self.shoulder_lift_link_z  # type: ignore

class ForcePush(Wrapper):
    """
    Force Push environment. You can apply forces to the robot's joints using the env.data.qfrc_applied
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

    def __init__(self,  **kwargs: dict[str, Any]):
        super().__init__(env = gym.make("FetchPush-v4", **kwargs))
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