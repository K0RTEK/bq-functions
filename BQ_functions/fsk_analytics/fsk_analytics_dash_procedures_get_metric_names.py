import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_metric_names(date, cluster_name, subcluster_name, campaign_name, attributes, tags, verify_itog, verify_itog_new):
    cluster_name = is_none(cluster_name)
    subcluster_name = is_none(subcluster_name)
    campaign_name = is_none(campaign_name)
    attributes = is_none(attributes)
    tags = is_none(tags)
    verify_itog = is_none(verify_itog)
    verify_itog_new = is_none(verify_itog_new)

    if cluster_name == 'cabinet':
        return 'cabinet'
    elif cluster_name in ['calls', 'leads', 'requests']:
        result = ','.join(filter(None, [
            'call' if cluster_name == 'calls' else '',
            'quality' if re.search('quality', attributes) and cluster_name == 'calls' else '',
            'commercial' if re.search('коммерческая|коммерция|псн аренда|мясницкая', campaign_name) and re.search('коммерческая', tags) and re.search('ца', tags) and re.search('покупка', tags) and re.search('quality', attributes) and cluster_name == 'calls' else '',
            'target' if re.search('гео', tags) and re.search('цена', tags) and re.search('ца', tags) and re.search('quality', attributes) and cluster_name == 'calls' else '',
            'vco' if (date < dt.date(2022, 10, 1) and verify_itog == 'ЦЕЛЕВОЙ') or (date >= dt.date(2022, 10, 1) and verify_itog_new in ['ЦЕЛЕВОЙ', 'УСЛОВНО ЦЕЛЕВОЙ']) else ''
        ]))
        return re.sub(r'[,]+', ',', result).strip(',')
    elif cluster_name == 'crm':
        if subcluster_name == 'naznachennye-pervichnye-vstrechi-ranee-vizity_1570095817':
            return 'appointed_visit'
        elif subcluster_name == 'sostoyavshiesya-pervichnye-vstrechi-ranee-sos_1570098045':
           return 'primary_visit'
        elif subcluster_name == 'db-podpisannye_1596117641':
           return 'signed_reserv'
        elif subcluster_name == 'db_1570099493':
           return 'paid_reserv'
        elif subcluster_name == 'sdelki-podpisannye-dkp-vseh-tipov-pomescheniy-_h1Nq1y':
           return 'signed_deal'
        elif subcluster_name == 'sdelki-oplata-30-dkp-_1570099875':
            return 'paid_deal'
    return None