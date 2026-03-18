from __future__ import annotations

import gymnasium as gym
import pytest

import rrls  # noqa: F401

reach_env = gym.make("rrls/robust-reach-v0")

@pytest.mark.parametrize("env", [reach_env])
def test_reach_change_params(env):
    desired_upperarm_roll_link_mass = 2.55
    desired_forearm_roll_link_mass = 1.95

    env.set_params(
        upperarm_roll_link_mass = desired_upperarm_roll_link_mass,
        forearm_roll_link_mass = desired_forearm_roll_link_mass
    )

    assert env.unwrapped.model.body_mass[14] == desired_upperarm_roll_link_mass
    assert env.unwrapped.model.body_mass[16] == desired_forearm_roll_link_mass

    expected_values = {
        "upperarm_roll_link_mass": desired_upperarm_roll_link_mass,
        "forearm_roll_link_mass": desired_forearm_roll_link_mass,
    }

    filtered_env_params = {
        k: v
        for k, v in env.get_params().items()
        if k in expected_values and v is not None
    }
    assert filtered_env_params == expected_values
    
