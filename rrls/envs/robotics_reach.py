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

class ForceReach(Wrapper):
    """
    Force Reach environment. You can apply forces to the robot using the env.data.xfrc_applied
    attribute. The parameters are:
        - shoulder_pan_joint
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
    
    # TODO:  correct variable names to the joints
    def set_params(
            self,
            shoulder_pan_joint: float | None = None,
    ):
        self.shoulder_pan_joint = shoulder_pan_joint
        self._change_params()

    def get_params(self):
        return{
            "shoulder_pan_joint": self.shoulder_pan_joint,
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
    ):
        if self.shoulder_pan_joint is not None:
            self.unwrapped.data.qfrc_applied[6] = shoulder_pan_joint  # type: ignore
        # if self.upperarm_roll_link_y is not None:
        #     self.unwrapped.data.xfrc_applied[14, 1] = upperarm_roll_link_y  # type: ignore
        # if self.upperarm_roll_link_z is not None:
        #     self.unwrapped.data.xfrc_applied[14, 2] = upperarm_roll_link_z  # type: ignore
