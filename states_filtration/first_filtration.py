"""
Description: This module provides utilties to perform the first stage of filtration of lattice states.
Filtration here is realized by G_z, as we impose Gauss law as i.e. G_z |\psi> = 0
"""

import numpy as np
from link_nums.link_num import n_links
from link_nums.link_up import n_link_up
from scipy.linalg import null_space

def n_links_list(recs_h: int, recs_v: int) -> list:
    """
    This function takes information about links attached to a given site in form of a tuple.
    As it is provided by the function n_links() in link_nums.link_num.
    Afterward this function forms a list of said tuples.

    :param recs_h: number of rectangles horizontally
    :param recs_v: number of rectangles vertically
    :return:
    n_links_list (list) : list of tuples
    """

    L_h = recs_h + 1
    L_v = 2 * recs_v + 2
    n_sites = L_h * L_v - 2

    n_links_list = []
    [n_links_list.append(n_links(s=_s, recs_h=recs_h, recs_v=recs_v)) for _s in range(n_sites)]
    return n_links_list


def prepared_list(recs_h: int, recs_v: int) -> list:
    L_h = recs_h + 1
    L_v = 2 * recs_v + 2

    n_sites = L_h * L_v - 2

    num_links = 1 + n_link_up(s=n_sites - 1, recs_h=recs_h, recs_v=recs_v)

    links = n_links_list(recs_h=recs_h, recs_v=recs_v)

    prepped_list = []
    for link_tuple in links:
        (i0, i1, i2, i3) = link_tuple

        # array to be used further in vertical stacking
        sample_arr = np.zeros(2 * int(num_links))

        # now do all the checking and translation into bigger array
        if i0 is not None:
            i0 = int(i0)
            sample_arr[2 * i0] = 1
        if i1 is not None:
            i1 = int(i1)
            sample_arr[2 * i1] = 1
        if i2 is not None:
            i2 = int(i2)
            sample_arr[2 * i2 + 1] = 1
        if i3 is not None:
            i3 = int(i3)
            sample_arr[2 * i3 + 1] = 1

        prepped_list.append(sample_arr)

    return prepped_list


def coefficient_matrix(recs_h: int, recs_v: int) -> np.array:
    prepped_list = prepared_list(recs_h=recs_h, recs_v=recs_v)
    result_array = np.vstack(prepped_list)

    return result_array


def states_gz_filtered(recs_h: int, recs_v: int)-> list:
    null_space_vectors: np.ndarray = null_space(coefficient_matrix(recs_h=recs_h, recs_v=recs_v))
    list_of_vectors = [null_space_vectors[:, i] for i in range(null_space_vectors.shape[1])]

    return list_of_vectors


recs_h = 2
recs_v = 2

res = states_gz_filtered(recs_h=recs_h, recs_v=recs_v)
print(res)
#TODO: implement finding free parameters, as it is done in the notebook.
# avoid fractions in vectors and shit, just cut off n_links tuple where needed
#TODO: afterwards, impose group constraint. It has to be applied during looping
# through free parameters, so that less possible states need to be checked.
quit()
A = coefficient_matrix(recs_h=recs_h, recs_v=recs_v)
print(A.shape)


ns_A = null_space(A)
print(ns_A.shape)


# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# num_links = 1 + n_link_up(s=n_sites-1, recs_h=recs_h, recs_v=recs_v)
#
#
# res = n_links_list(recs_h=recs_h, recs_v=recs_v)
# print(res)


# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(n_links(s=_s, recs_h=2, recs_v=2)) for _s in range(n_sites)]