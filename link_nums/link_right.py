import numpy as np


def n_link_right_recs_h_even(s: int, recs_h: int, recs_v: int):

    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    delta_s = (s - (2 * L_h - 1)) % L_h
    # contribution from rows 0 and 1
    ctrb_01 = 2 * L_h - 2
    ctrb_middle = ((s - (2 * L_h - 1)) // L_h) * ((L_h//2) * 3 + 1)

    if s % 2 == 1:
        return None

    # 0-th row
    elif s < L_h-1:
        return s / 2

    # 1-st row
    elif s == 2 * L_h - 2:
        return None

    elif s == L_h - 1:
        return 0.5 * (L_h - 1)

    elif (s > L_h - 1) and (s < 2 * L_h - 2):
        return 0.5 * (L_h - 1) + 1.5 * (s - (L_h - 1)) - 1

    # >1 row
    elif delta_s == (L_h - 1):
        return None

    elif delta_s % 2 == 0:
        return ctrb_01 + ctrb_middle + 1.5 * delta_s

    elif delta_s % 2 == 1:
        return ctrb_01 + ctrb_middle + 1.5 * (delta_s - 1) + 1


def n_link_right_recs_h_odd(s: int, recs_h: int, recs_v: int):
    L_h = recs_h + 1
    L_v = 2*recs_v + 2
    n_sites = L_h * L_v - 2

    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    delta_s = (s - (2 * L_h - 2)) % L_h
    # contribution from rows 0 and 1
    ctrb_01 = 2 * L_h - 3
    # k is number of the given row, where s is.
    # counting is such that k=0 is the first full row after 0th and 1st
    k = (s - (2*L_h - 2))//L_h
    ctrb_middle = 3*k*(L_h//2) - (k + (k & 1))/2

    # 0-th row
    if (s < (L_h-2)) and ((s % 2) == 0):
        return s / 2

    elif (s < (L_h-2)) and ((s % 2) == 1):
        return None

    # 1-st row
    elif (s == (L_h - 2)):
        return (L_h - 2) / 2
    elif (s > (L_h - 2)) and (s < (2 * L_h - 2)) and ((s % 2) == 0):
        return (L_h - 2) / 2 + 1.5 * (s - (L_h - 2)) - 1
    elif (s > (L_h - 2)) and (s < (2 * L_h - 2)) and ((s % 2) == 1):
        return None

    # >1 row
    # k even
    elif ((k % 2) == 0) and ((s % 2) == 0):
        return None
    elif ((k % 2) == 0) and delta_s == (L_h - 1):
        return None
    elif ((k % 2) == 0) and ((s % 2) == 1):
        return ctrb_01 + ctrb_middle + 1.5 * (delta_s - 1) + 1

    # k odd
    elif ((k % 2) == 1) and ((s % 2) == 1):
        return None
    elif ((k % 2) == 1) and ((s % 2) == 0):
        return ctrb_01 + ctrb_middle + 1.5 * delta_s


def n_link_right_recs_h_1(s: int, recs_h: int, recs_v: int):
    L_h = recs_h + 1
    L_v = 2*recs_v + 1
    n_sites = L_h * L_v


    if (s < 0) or (s > n_sites - 1):
        raise ValueError(f"Argument 's' can only take values from 0 till {n_sites - 1}.")

    if (s == 0):
        return 0
    elif ((s % 4) == 0) and (s > 0):
        return 3 + 5 * ((s//4) - 1)
    else:
        return None


def n_link_right(s: int, recs_h: int, recs_v: int):
    if (recs_h == 1):
        return n_link_right_recs_h_1(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 0:
        return n_link_right_recs_h_even(s=s, recs_h=recs_h, recs_v=recs_v)
    elif (recs_h % 2) == 1:
        return n_link_right_recs_h_odd(s=s, recs_h=recs_h, recs_v=recs_v)





# recs_h = 3
# recs_v = 1
#
# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(f"s={_s}-> ", "link_right = ", n_link_right(s=_s, recs_h=recs_h, recs_v = recs_v)) for _s in range(n_sites)]
