import re
import datetime as dt

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def social_clarification(campaign, date):
    campaign = is_none(campaign)
    if date <= dt.date(2022, 12, 31):
        return 'NaN'
    else:
        if re.search(r'14d_', campaign):
            return '14 дней'
        elif re.search(r'10d_', campaign):
            return '10 дней'
        elif re.search(r'7d_|pf_m_dir_kw_s22_msk_23-55_multi_cross_mt|pf_m_dir_kw_s22_rf_23-55_multi_cross_mt|pf_m_dir_kw_flip4_msk_23-55_multi_cross_mt|pf_m_dir_kw_flip4_rf_23-55_multi_cross_mt|pf_m_dir_kw_fold4_msk_23-55_multi_cross_mt|pf_m_dir_kw_fold4_rf_23-55_multi_cross_mt', campaign):
            return '7 дней'
        elif re.search(r'phone_', campaign):
            return 'Интерес к покупке мобильного телефона'
        elif re.search(r'checkout', campaign):
            return 'Начало оформления заказа'
        elif re.search(r'cart', campaign):
            return 'Корзина'
        elif re.search(r'auto', campaign):
            return 'Автоинтересы'
        elif re.search(r'brand-3d', campaign):
            return 'Брендовые ключи 3 дня'
        elif re.search(r'view', campaign):
            return 'Просмотр'
        elif re.search(r'action', campaign):
            return 'Любое действие'
        elif re.search(r'site14', campaign):
            return 'Посещение сайта в течение 14 дней'
        else:
            return 'NaN'