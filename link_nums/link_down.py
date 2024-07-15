import numpy as np
from link_up import n_link_up as n_l2


def n_link_down_recs_h_even(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s > n_sites - L_h - 1):
        return None
    else:
        return n_l2(s=s+L_h, recs_h=recs_h, recs_v=recs_v)


def n_link_down_recs_h_odd(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s > (n_sites - L_h - 1)):
        return None
    elif (s < (L_h - 2)):
        return n_l2(s=s+L_h-1, recs_h=recs_h, recs_v=recs_v)
    else:
        return n_l2(s=s+L_h, recs_h=recs_h, recs_v=recs_v)


def n_link_down_recs_h_1(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2 * recs_v + 1
    n_sites = L_h * L_v

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s > (n_sites - L_h - 1)):
        return None
    else:
        return n_l2(s=s+L_h, recs_h=recs_h, recs_v=recs_v)


def n_link_down(s: int, recs_h: int, recs_v: int):
    if (recs_h == 1):
        return n_link_down_recs_h_1(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 0:
        return n_link_down_recs_h_even(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 1:
        return n_link_down_recs_h_odd(s=s, recs_h=recs_h, recs_v=recs_v)

# recs_h = 3
# recs_v = 2
#
# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(f"s={_s}-> ", "link_right = ", n_link_down(s=_s, recs_h=recs_h, recs_v = recs_v)) for _s in range(n_sites)]


