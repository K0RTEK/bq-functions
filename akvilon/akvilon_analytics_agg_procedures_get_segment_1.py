import re
from datetime import date

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


def get_segment_1(current_date, channel, utm_campaign):
    channel = is_none(channel)
    utm_campaign = is_none(utm_campaign)
    variables_var_prgrm_channel ='Programmatic/OLV'
    variables_var_prgrm_yandex = 'Яндекс'
    variables_var_cont_channel = 'Контекстная реклама'
    # Программатик
    if channel == variables_var_prgrm_channel + variables_var_prgrm_yandex:
        if utm_campaign is None:
            return None
        elif re.search(r'video', utm_campaign.strip()):
            return 'Видео'
        else:
            return 'Баннеры'

    # Яндекс Директ
    elif channel == variables_var_cont_channel:
        if date(2023, 7, 1) <= current_date <= date(2024, 1, 31):
            if re.search(r'(ya_|ya_mg_)s_indy_brand', utm_campaign) and not re.search(r'signal|mg_indy',
                                                                                              utm_campaign):
                return 'Бренд'
            elif re.search(r'(ya_|ya_mg_)s_indy_geo', utm_campaign) and not re.search(r'NONE',
                                                                                              utm_campaign):
                return 'Гео'
            elif re.search(r'(ya_|ya_mg_)s_indy_remarketing', utm_campaign) and not re.search(r'NONE',
                                                                                                      utm_campaign):
                return 'Ретаргетинг'
            elif re.search(r'(ya_|ya_mg_)s_indy_compet', utm_campaign) and not re.search(r'NONE',
                                                                                                 utm_campaign):
                return 'Конкуренты'
            elif re.search(r'(ya_|ya_mg_)s_indy_general', utm_campaign) and not re.search(r'NONE',
                                                                                                  utm_campaign):
                return 'Общие'
            elif re.search(r'(ya_|ya_mg_)s_indy_mkb', utm_campaign) and not re.search(r'NONE',
                                                                                              utm_campaign):
                return 'МКБ'
            elif re.search(r'(ya_|ya_mg_)n_indy_compet', utm_campaign) and not re.search(r'NONE',
                                                                                                 utm_campaign):
                return 'Конкуренты'
            elif re.search(r'(ya_|ya_mg_)n_indy_all', utm_campaign) and not re.search(r'test',
                                                                                              utm_campaign):
                return 'Объединенная РК'
            elif re.search(r'(ya_|ya_mg_)n_indy_all_mmo_test1', utm_campaign) and not re.search(r'NONE',
                                                                                                        utm_campaign):
                return 'Тест Аквилон'
            elif re.search(r'(ya_|ya_mg_)n_indy_all_mmo_test2', utm_campaign) and not re.search(r'NONE',
                                                                                                        utm_campaign):
                return 'Тест Аквилон'
            elif re.search(r'(ya_|ya_mg_)n_indy_remarketing', utm_campaign) and not re.search(r'NONE',
                                                                                                      utm_campaign):
                return 'Ретаргетинг'
            elif re.search(r'(ya_|ya_mg_)mc_indy', utm_campaign) and not re.search(
                    r'ya_mc_indy_feed-catalog_mmo', utm_campaign):
                return 'Мастер Кампаний'
            elif re.search(r'(ya_|ya_mg_)n_indy_interests', utm_campaign) and not re.search(r'NONE',
                                                                                                    utm_campaign):
                return 'Тест Интересы'
            elif re.search(r'(ya_|ya_mg_)s_indy_brand-gk', utm_campaign) and not re.search(r'NONE',
                                                                                                   utm_campaign):
                return 'Бренд Аквилон'
            elif re.search(r'(ya_|ya_mg_)s_indy_brand_rf', utm_campaign) and not re.search(r'NONE',
                                                                                                   utm_campaign):
                return 'Бренд Регионы'
            elif re.search(r'(ya_|ya_mg_)n_indy_all_rf', utm_campaign) and not re.search(r'NONE',
                                                                                                 utm_campaign):
                return 'Объединенная РК Регионы'
            elif re.search(r'(ya_|ya_mg_)n_indy_ipoteka_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                      utm_campaign):
                return 'Ипотека'
            elif re.search(r'(ya_|ya_mg_)s_indy_compet_mkb_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                         utm_campaign):
                return 'МКБ Конкуренты'
            elif re.search(r'(ya_|ya_mg_)mc_indy_feed-catalog_mmo', utm_campaign) and not re.search(
                    r'ya_mc_indy', utm_campaign):
                return 'Товарная кампания'
            elif re.search(r'(ya_|ya_mg_)n_indy_remarketing_rf', utm_campaign) and not re.search(r'NONE',
                                                                                                         utm_campaign):
                return 'Ретаргетинг на РФ'
            elif re.search(r'(ya_|ya_mg_)n_indy_all-mob_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                      utm_campaign):
                return 'Мобильная кампания'
            elif re.search(r'(ya_|ya_mg_)tg_indy_all_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                   utm_campaign):
                return 'Телеграм тест'
            elif re.search(r'(ya_|ya_mg_)performance_indy_all_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                            utm_campaign):
                return 'Перфоманс'

        # Обрабатываем периоды с 2024-02-01
        elif current_date >= date(2024, 2, 1):
            if re.search(r'ya_mg_performance_indy_all-new_mmo', utm_campaign) and not re.search(r'NONE',
                                                                                                        utm_campaign):
                return 'ЕПК'
            elif re.search(r'(ya_|ya_mg_)s_indy_brand', utm_campaign) and not re.search(r'NONE',
                                                                                                utm_campaign):
                return 'Бренд'
            elif re.search(r'(ya_|ya_mg_)mc_indy|ya_mg_performance_indy', utm_campaign) and not re.search(
                    r'NONE', utm_campaign):
                return 'Мастер Кампаний'
            elif re.search(r'(ya_|ya_mg_)s_indy', utm_campaign) and not re.search(r'brand',
                                                                                          utm_campaign):
                return 'Поиск'
            elif re.search(r'(ya_|ya_mg_)n_indy', utm_campaign) and not re.search(r'NONE',
                                                                                          utm_campaign):
                return 'РСЯ'
            elif re.search(r'ya_mg_s_signal_brand', utm_campaign) and not re.search(r'NONE',
                                                                                            utm_campaign):
                return 'Бренд'
            elif re.search(r'ya_mg_mc_signal', utm_campaign) and not re.search(r'NONE', utm_campaign):
                return 'Мастер Кампаний'
            elif re.search(r'ya_mg_s_signal', utm_campaign) and not re.search(r'brand', utm_campaign):
                return 'Поиск'
            elif re.search(r'ya_mg_n_signal_remarketing', utm_campaign) and not re.search(r'NONE',
                                                                                                  utm_campaign):
                return 'Ретаргетинг'
            elif re.search(r'ya_mg_n_signal', utm_campaign) and not re.search(r'remarketing',
                                                                                      utm_campaign):
                return 'РСЯ'
            elif re.search(r'ya_mg_s_beside_brand', utm_campaign) and not re.search(r'akvilon_beside_brand',
                                                                                            utm_campaign):
                return 'Бренд'
            elif re.search(r'ya_mg_mc_beside', utm_campaign) and not re.search(r'NONE', utm_campaign):
                return 'Мастер Кампаний'
            elif re.search(r'ya_mg_s_beside', utm_campaign) and not re.search(r'brand', utm_campaign):
                return 'Поиск'
            elif re.search(r'ya_mg_mkb_beside', utm_campaign):
                return 'Поиск'
            elif re.search(r'ya_mg_n_beside_remarketing', utm_campaign) and not re.search(r'NONE',
                                                                                                  utm_campaign):
                return 'Ретаргетинг'
            elif re.search(r'ya_mg_n_beside', utm_campaign):
                return 'РСЯ'
        return 'Общий'

    return 'Общий'
