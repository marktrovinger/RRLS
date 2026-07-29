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
    Force Reach environment. You can apply friction and damping to the robot's joints using the env.unwrapped.model.dof_frictionloss
    or env.unwrapped.model.dof_damping attributes. This wraps the "sparse" reward environment. The parameters are:
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
        "shoulder_pan_joint":    6,
        "shoulder_lift_joint":   7,
        "upperarm_roll_joint":   8,
        "elbow_flex_joint":      9,
        "forearm_roll_joint":   10,
        "wrist_flex_joint":     11,
        "wrist_roll_joint":     12,
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
        self._change_params()

    def set_params(
            self,
            shoulder_pan_frictionloss: float | None = None,
            shoulder_pan_damping: float | None = None,
            shoulder_lift_frictionloss: float | None = None,
            shoulder_lift_damping: float | None = None,
            elbow_flex_frictionloss: float | None = None,
            elbow_flex_damping: float | None = None,
            upperarm_roll_frictionloss: float | None = None,
            upperarm_roll_damping: float | None = None,
            forearm_roll_frictionloss: float | None = None,
            forearm_roll_damping: float | None = None,
            wrist_flex_frictionloss: float | None = None,
            wrist_flex_damping: float | None = None,
            wrist_roll_frictionloss: float | None = None,
            wrist_roll_damping: float | None = None,

    ):
        self.shoulder_pan_frictionloss = shoulder_pan_frictionloss
        self.shoulder_pan_damping = shoulder_pan_damping
        self.shoulder_lift_frictionloss = shoulder_lift_frictionloss
        self.shoulder_lift_damping = shoulder_lift_damping
        self.upperarm_roll_frictionloss = upperarm_roll_frictionloss
        self.upperarm_roll_damping = upperarm_roll_damping
        self.elbow_flex_frictionloss = elbow_flex_frictionloss
        self.elbow_flex_damping = elbow_flex_damping
        self.forearm_roll_frictionloss = forearm_roll_frictionloss
        self.forearm_roll_damping = forearm_roll_damping
        self.wrist_flex_frictionloss = wrist_flex_frictionloss
        self.wrist_flex_damping = wrist_flex_damping
        self.wrist_roll_frictionloss = wrist_roll_frictionloss
        self.wrist_roll_damping = wrist_roll_damping
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
    
    def _change_params(
            self,
            shoulder_pan_frictionloss: float | None = None,
            shoulder_pan_damping: float | None = None,
            shoulder_lift_frictionloss: float | None = None,
            shoulder_lift_damping: float | None = None,
            elbow_flex_frictionloss: float | None = None,
            elbow_flex_damping: float | None = None,
            upperarm_roll_frictionloss: float | None = None,
            upperarm_roll_damping: float | None = None,
            forearm_roll_frictionloss: float | None = None,
            forearm_roll_damping: float | None = None,
            wrist_flex_frictionloss: float | None = None,
            wrist_flex_damping: float | None = None,
            wrist_roll_frictionloss: float | None = None,
            wrist_roll_damping: float | None = None,
    ):
        if self.shoulder_pan_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["shoulder_pan_joint"]] = shoulder_pan_frictionloss  # type: ignore
        if self.shoulder_pan_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["shoulder_pan_joint"]] = shoulder_pan_damping  # type: ignore
        if self.shoulder_lift_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["shoulder_lift_joint"]] = shoulder_lift_frictionloss  # type: ignore
        if self.shoulder_lift_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["shoulder_lift_joint"]] = shoulder_lift_damping  # type: ignore
        if self.upperarm_roll_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["upperarm_roll_joint"]] = upperarm_roll_frictionloss  # type: ignore
        if self.upperarm_roll_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["upperarm_roll_joint"]] = upperarm_roll_damping  # type: ignore
        if self.elbow_flex_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["elbow_flex_joint"]] = elbow_flex_frictionloss  # type: ignore
        if self.elbow_flex_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["elbow_flex_joint"]] = elbow_flex_damping  # type: ignore
        if self.forearm_roll_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["forearm_roll_joint"]] = forearm_roll_frictionloss  # type: ignore
        if self.forearm_roll_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["forearm_roll_joint"]] = forearm_roll_damping  # type: ignore
        if self.wrist_flex_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["wrist_flex_joint"]] = wrist_flex_frictionloss  # type: ignore
        if self.wrist_flex_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["wrist_flex_joint"]] = wrist_flex_damping  # type: ignore
        if self.wrist_roll_frictionloss is not None:
            self.self.unwrapped.model.dof_frictionloss[self.ARM_DOF_INDICES["wrist_roll_joint"]] = wrist_roll_frictionloss  # type: ignore
        if self.wrist_roll_damping is not None:
            self.self.unwrapped.model.dof_damping[self.ARM_DOF_INDICES["wrist_roll_joint"]] = wrist_roll_damping  # type: ignore