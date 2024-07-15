import numpy as np
from link_right import n_link_right as n_l1


def n_link_up_recs_h_even(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s < L_h):
        return None
    elif (s == L_h):
        return n_l1(s=L_h-1, recs_h=recs_h, recs_v=recs_v) + 1

    # last column elements that are even
    elif (((s - (L_h - 1)) % L_h) == (L_h - 1)) and ((s % 2) == 0):
        return n_l1(s=s - 2, recs_h=recs_h, recs_v=recs_v) + 3

    # first column elements that are odd
    elif (((s - (L_h - 1)) % L_h) == 0) and ((s % 2) == 1):
        return n_l1(s=s + 1, recs_h=recs_h, recs_v=recs_v) - 1

    # ordinary even and odd cases
    elif ((s % 2) == 0):
        return n_l1(s=s, recs_h=recs_h, recs_v=recs_v) + 1
    elif ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v) + 2


def n_link_up_recs_h_odd(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    # special cases for rows 0 and 1
    if (s < (L_h -1)):
        return None
    elif (s == (L_h - 1)):
        return n_l1(s=L_h - 2, recs_h=recs_h, recs_v=recs_v) + 1
    elif (s == (2*L_h - 3)):
        return None
    elif (s > (L_h - 1)) and (s < (2*L_h - 3)) and ((s % 2) == 0):
        return n_l1(s=s, recs_h=recs_h, recs_v=recs_v) + 1
    elif (s > (L_h - 1)) and (s < (2*L_h - 3)) and ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v) + 2

    # special case first and last column even rows
    elif (((s - (2*L_h - 2)) % L_h) == 0) and ((((s - (2*L_h - 2)) // L_h) % 2) == 0):
        return n_l1(s=s+1, recs_h=recs_h, recs_v=recs_v) - 1
    elif (((s - (2*L_h - 2)) % L_h) == (L_h - 1)) and ((((s - (2*L_h - 2)) // L_h) % 2) == 0):
        return n_l1(s=s-2, recs_h=recs_h, recs_v=recs_v) + 3

    # normal case, even rows
    elif ((((s - (2*L_h - 2)) // L_h) % 2) == 0) and ((s % 2) == 0):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v) + 2
    elif ((((s - (2*L_h - 2)) // L_h) % 2) == 0) and ((s % 2) == 1):
        return n_l1(s=s, recs_h=recs_h, recs_v=recs_v) + 1

    # normal case, odd rows
    elif ((((s - (2*L_h - 2)) // L_h) % 2) == 1) and ((s % 2) == 0):
        return n_l1(s=s, recs_h=recs_h, recs_v=recs_v) + 1
    elif ((((s - (2*L_h - 2)) // L_h) % 2) == 1) and ((s % 2) == 1):
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v) + 2


def n_link_up_recs_h_1(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2 * recs_v + 1
    n_sites = L_h * L_v

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s < L_h):
        return None
    elif (s % 4) == 2:
        return n_l1(s=s+2, recs_h=recs_h, recs_v=recs_v) - 2
    elif (s % 4) == 3:
        return n_l1(s=s+1, recs_h=recs_h, recs_v=recs_v) - 1
    elif (s % 4) == 0:
        return n_l1(s=s, recs_h=recs_h, recs_v=recs_v) + 1
    elif (s % 4) == 1:
        return n_l1(s=s-1, recs_h=recs_h, recs_v=recs_v) + 2



def n_link_up(s: int, recs_h: int, recs_v: int):
    if (recs_h == 1):
        return n_link_up_recs_h_1(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 0:
        return n_link_up_recs_h_even(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 1:
        return n_link_up_recs_h_odd(s=s, recs_h=recs_h, recs_v=recs_v)

# recs_h = 3
# recs_v = 2
#
# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(f"s={_s}-> ", "link_right = ", n_link_up(s=_s, recs_h=recs_h, recs_v = recs_v)) for _s in range(n_sites)]

