import numpy as np
from link_nums.link_right import n_link_right as n_l1


def n_link_left_recs_h_even(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if ((s % 2) == 0):
        return None
    elif ((s - (2*L_h - 1)) % L_h) == 0:
        return None
    elif ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v)


def n_link_left_recs_h_odd(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    # special cases for rows 0 and 1
    if (s < (2*L_h - 2)) and ((s % 2) == 0):
        return None
    elif (s < (2*L_h - 2)) and ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v)

    # special case for first column
    elif ((s - (2*L_h - 2)) % L_h) == 0:
        return None

    # normal cases for even and odd rows, counting from after row 1
    elif (((s - (2*L_h - 2)) // L_h) % 2 == 0) and ((s % 2) == 1):
        return None
    elif (((s - (2*L_h - 2)) // L_h) % 2 == 0) and ((s % 2) == 0):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v)
    elif (((s - (2*L_h - 2)) // L_h) % 2 == 1) and ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v)
    elif (((s - (2*L_h - 2)) // L_h) % 2 == 1) and ((s % 2) == 0):
        return None


def n_link_left_recs_h_1(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 1
    n_sites = L_h * L_v


    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s % 4) == 1:
        return n_l1(s=s - 1, recs_h=recs_h, recs_v=recs_v)
    else:
        return None


def n_link_left(s: int, recs_h: int, recs_v: int):
    if (recs_h == 1):
        return n_link_left_recs_h_1(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 0:
        return n_link_left_recs_h_even(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 1:
        return n_link_left_recs_h_odd(s=s, recs_h=recs_h, recs_v=recs_v)




# recs_h = 4
# recs_v = 2
#
# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(f"s={_s}-> ", "link_right = ", n_link_left(s=_s, recs_h=recs_h, recs_v = recs_v)) for _s in range(n_sites)]

