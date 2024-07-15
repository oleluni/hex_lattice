from link_right import n_link_right as n_l1
from link_up import n_link_up as n_l2
from link_left import n_link_left as n_l3
from link_down import n_link_down as n_l4


def n_links(s: int, recs_h: int, recs_v: int):
    n1 = n_l1(s=s, recs_h=recs_h, recs_v=recs_v)
    n2 = n_l2(s=s, recs_h=recs_h, recs_v=recs_v)
    n3 = n_l3(s=s, recs_h=recs_h, recs_v=recs_v)
    n4 = n_l4(s=s, recs_h=recs_h, recs_v=recs_v)

    return (n1, n2, n3, n4)


# recs_h = 3
# recs_v = 2
#
# L_h = recs_h + 1
# L_v = 2 * recs_v + 2
# n_sites = L_h * L_v - 2
#
# [print(f"s={_s}-> ", "link_right = ", n_links(s=_s, recs_h=recs_h, recs_v = recs_v)) for _s in range(n_sites)]

