import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_source_type(date, utm_source, utm_medium, utm_campaign, utm_content, term):
    utm_source = is_none(utm_source)
    utm_medium = is_none(utm_medium)
    utm_campaign = is_none(utm_campaign)
    utm_content = is_none(utm_content)
    term = is_none(term)

    if (re.search(r'src\|context|src\|{n}|src%7ccontext|src:context|st\|context|st%7ccontext|st:context|st\|{n}|st%7c{n}|src%7c{n}|src:{n}|st:{n}', term, re.IGNORECASE) or
        re.search(r'src\|context|src\|{n}|src%7ccontext|src:context|st\|context|st%7ccontext|st:context|st\|{n}|st%7c{n}|src%7c{n}|src:{n}|st:{n}', utm_content, re.IGNORECASE)):
        return 'ad_network'
    elif (re.search(r'src\|search|src\|g|src%7csearch|src:search|st\|search|st%7csearch|st:search|st\|s|st:s|st\|g|src:g|src\|s|src:s|src%7cs|src%7cg|st%7cs|st%7cg|src:d|src\|d|src%7cd|st:d|st\|d|st%7cd', term, re.IGNORECASE) or
          re.search(r'src\|search|src\|g|src%7csearch|src:search|st\|search|st%7csearch|st:search|st\|s|st:s|st\|g|src:g|src\|s|src:s|src%7cs|src%7cg|st%7cs|st%7cg|src:d|src\|d|src%7cd|st:d|st\|d|st%7cd', utm_content, re.IGNORECASE)):
        return 'search'
    else:
        return 'unknown'