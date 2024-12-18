def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_ga_fraude(timeOnSite, transactions):
    timeOnSite = is_none(timeOnSite)
    transactions = is_none(transactions)
    if (timeOnSite <= 61 and transactions > 6) or (61 < timeOnSite <= 2076 and transactions > 14):
        return True
    else:
        return None