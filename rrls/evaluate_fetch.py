from __future__ import annotations

import itertools
from typing import Annotated, Callable

import numpy as np

from ._interface import ModifiedParamsEnv
from .envs import (
    ReachParamsBound,
    ForceReach
)
from concurrent.futures import ProcessPoolExecutor


def generate_evaluation_set(
    modified_env: Callable[[], ModifiedParamsEnv],
    param_bounds: dict[str, Annotated[list[float], 2]],
    nb_mesh_dim: int = 10,
) -> list[ModifiedParamsEnv]:
    """
    Generate a list of environments to be used for evaluation by meshing the parameter space.

    Args:
        modified_env (Callable[[], ModifiedParamsEnv]): A function that returns a modified environment.
        param_bounds (dict[str, Annotated[list[float], 2]]): Parameter boundaries.
        nb_mesh_dim (int): Number of mesh dimensions.

    Returns:
        list[ModifiedParamsEnv]: A list of environments to be used for evaluation.
    """
    # Generate all combinations of environments given the mesh
    eval_envs = []
    parameters_values = {
        parameter_name: np.arange(
            start=bound_value[0],
            stop=bound_value[1],  # type: ignore
            step=(bound_value[1] - bound_value[0]) / nb_mesh_dim,  # type: ignore
        ).tolist()
        for parameter_name, bound_value in param_bounds.items()
    }
    for values in itertools.product(*parameters_values.values()):
        params = dict(zip(parameters_values.keys(), values))
        env = modified_env(**params)
        #print(f"Finished creating '{modified_env} with {params}.")
        eval_envs.append(env)
    
    return eval_envs

#if __name__ == "__main__":
    # data = {"modified_env": ForceReach, 
    #         "param_bounds":ReachParamsBound.SHOULDER_FRICTION.value,
    #         "nb_mesh_dim": 2
    #         }
    # with ProcessPoolExecutor() as executor:
    #     EVALUATION_FORCE_REACH_SHOULDER = executor.map(generate_evaluation_set, data)
EVALUATION_FORCE_REACH_SHOULDER = generate_evaluation_set(
    modified_env=ForceReach, # type: ignore
    param_bounds=ReachParamsBound.SHOULDER_FRICTION.value,
    nb_mesh_dim=10
)

    # EVALUATION_FORCE_REACH_ELBOW = generate_evaluation_set(
    #     modified_env=ForceReach, # type: ignore
    #     param_bounds=ReachParamsBound.ELBOW_FRICTION.value,
    #     nb_mesh_dim=2
    # )

    # EVALUATION_FORCE_REACH_WRIST = generate_evaluation_set(
    #     modified_env=ForceReach, # type: ignore
    #     param_bounds=ReachParamsBound.WRIST_FRICTION.value,
    #     nb_mesh_dim=2
    # )

    # EVALUATION_FORCE_REACH_ARM = generate_evaluation_set(
    #     modified_env=ForceReach, # type: ignore
    #     param_bounds=ReachParamsBound.WHOLE_ARM_FRICTION.value,
    #     nb_mesh_dim=2
    # )
