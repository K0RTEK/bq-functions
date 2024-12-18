import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_metric_names(date, cluster_name, subcluster_name, campaign_name, attributes, tags, verify_itog,
                     verify_itog_new):

    cluster_name = is_none(cluster_name)
    campaign_name = is_none(campaign_name)
    attributes = is_none(attributes)
    tags = is_none(tags)
    verify_itog_new = is_none(verify_itog_new)
    verify_itog = is_none(verify_itog)

    if cluster_name == 'cabinet':
        return 'cabinet'
    elif cluster_name in ('calls', 'leads', 'requests'):
        return 'vco' if verify_itog else ''
    elif cluster_name == 'crm':
        if not is_none(subcluster_name):
            if subcluster_name == 'naznachennye-pervichnye-vstrechi':
                return 'appointed_visit'
            else:
                return f"NaN - {subcluster_name}"

    return None  # Default return if none of the conditions match