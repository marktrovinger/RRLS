from __future__ import annotations

import gymnasium as gym
import pytest

import rrls  # noqa: F401

reach_env = gym.make("rrls/robust-reach-v0")

@pytest.mark.parametrize("env", [reach_env])
def test_reach_change_params(env):
    desired_upperarm_mass = 3.0
    desired_lowerarm_mass = 4.0
    #desired_frontrightlegmass = 5.0
