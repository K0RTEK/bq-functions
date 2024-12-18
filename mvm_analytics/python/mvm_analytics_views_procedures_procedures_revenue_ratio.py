import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def revenue_ratio(mv_eldo_cpa):
    mv_eldo_cpa = is_none(mv_eldo_cpa)
    if mv_eldo_cpa == 'эльдорадо':
        return 0.53
    elif mv_eldo_cpa == 'м.видео':
        return 1.2776
    elif mv_eldo_cpa == 'cpa':
        return 1.79