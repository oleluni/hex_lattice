"""
Description: This module provides utilties to perform the first stage of filtration of lattice states.
Filtration here is realized by G_z, as we impose Gauss law as i.e. G_z |\psi> = 0
"""

import numpy as np
import sympy as sp
from link_nums.link_num import n_links as get_links
from link_nums.link_up import n_link_up
from scipy.linalg import null_space


def generate_state_array(recs_h: int, recs_v: int):
    L_h = recs_h + 1
    L_v = 2 * recs_v + 2
    num_sites = L_h * L_v - 2
    num_links = int(1 + n_link_up(s=num_sites - 1, recs_h=recs_h, recs_v=recs_v))

    # Create the symbolic variables for mL and mR
    mL = [sp.symbols(f'mL{i}') for i in range(num_links)]
    mR = [sp.symbols(f'mR{i}') for i in range(num_links)]

    # Initialize the state array with None
    state_array = [None] * (2 * num_links)
    for i in range(num_links):
        state_array[2 * i] = mL[i]
        state_array[2 * i + 1] = mR[i]

    # Dictionary to store the constraints (site: [links])
    constraints = {}

    # Create the Gauss law constraints for each site
    for site in range(num_sites):
        links = get_links(s=site, recs_h=recs_h, recs_v=recs_v)

        site_constraints = [
            mL[int(links[0])] if links[0] is not None else None,
            mL[int(links[1])] if links[1] is not None else None,
            mR[int(links[2])] if links[2] is not None else None,
            mR[int(links[3])] if links[3] is not None else None
        ]

        constraints[site] = site_constraints

    # Fill the state array based on constraints
    free_parameters = []
    # Iterate through the constraints dictionary
    for site, constraint in constraints.items():
        # Initialize a list to store the non-None constraints
        non_none_constraints = [link for link in constraint if link is not None]

        # Deal with the dependencies
        dependent_var = non_none_constraints[-1]
        last_char = int(str(dependent_var)[2:])  # i.e. reading 2 as int off mR2

        independent_vars = non_none_constraints[:-1]
        dependent_expr = -sum(independent_vars)
        # Update state_array with the dependent expression
        for i, link in enumerate(constraint): # TODO: this constraint or the non_none_constraints?
            if link == dependent_var:
                if i == 0 or i == 1:
                    index = 2 * last_char
                else:
                    index = 2 * last_char + 1
                # print(state_array[index])
                # print(dependent_expr)
                # quit()
                state_array[index] = dependent_expr

        # Write down the free parameters
        free_parameters.extend(independent_vars)

    return state_array, free_parameters



recs_h = 2
recs_v = 2


state_array, free_parameters = generate_state_array(recs_h=recs_h, recs_v=recs_v)

print("State Array:", state_array)
print("Free Parameters:", free_parameters)
