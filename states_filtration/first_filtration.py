"""
Description: This module provides utilties to perform the first stage of filtration of lattice states.
Filtration here is realized by G_z, as we impose Gauss law as i.e. G_z |\psi> = 0
"""

import numpy as np
from link_nums.link_num import n_links
from link_nums.link_up import n_link_up


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




recs_h = 2
recs_v = 2

L_h = recs_h + 1
L_v = 2 * recs_v + 2
n_sites = L_h * L_v - 2

num_links = 1 + n_link_up(s=n_sites-1, recs_h=recs_h, recs_v=recs_v)


res = n_links_list(recs_h=recs_h, recs_v=recs_v)
print(res)


# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(n_links(s=_s, recs_h=2, recs_v=2)) for _s in range(n_sites)]