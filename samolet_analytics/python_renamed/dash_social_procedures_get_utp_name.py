import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()

def get_segment(parameter):
    parameter = is_none(parameter)

    if re.search(r'_ipt|_famipt|_IT-ipt|_ipt.lgt|_ipt.legko|_ipt.transh|_ipt1R|_fam.mltry.ipt|_ipt.lgt|_dom.otdel-IT-ipt|_kv-life-ipt|_war-ipt|_ipt-minpay|_dig-ipt', parameter):
        return 'Ипотека'
    elif re.search(r'_dom.mbl-minpay|_dom.otdel-minpay', parameter):
        return 'Мин платеж'
    elif re.search(r'_bron|_st.sale|_newkorp|_new-kv|_new-apart', parameter):
        return 'Старт продаж'
    elif re.search(r'_minprice|_ski-minprice|_kv.mck-minprice|_kv.nab-minprice|_mbl-minprice-yug|_mbl-minprice-cl-yug|_kv.centr-minprice|_dom.home-appl-minprice|_kv.metro-minprice|_dom.home-appl-rassr-minprice|_kv.otdel-minprice|_mbl-minprice|_dom.otdel-city-nov.sh-minprice|_dom.otdel-comfort-full.life-minprice|_dom.otdel-frame-minprice|_dom.otdel-stone-minprice|_dom.water-minprice|_dom.shale-minprice|_dom.otdel-minprice|_dom.mbl-city.infr-minprice|_dom.mbl-minprice|_start-minprice|_start-minpay|_ap.mbl-minprice|_apart.ot-minprice|_apart.bk-minprice|_reka-minprice|_kv-life-minprice|_no.otdel-minprice|_key24.minprice|_1minprice|_2minprice|_ap.2minprice|_2k-life-minprice', parameter):
        return 'Минимальная стоимость'
    elif re.search(r'_apart.bk', parameter):
        return 'Аппартаменты'
    elif re.search(r'_sdacha24|_sdacha25|_zas24|_zas25|_key24|_key25|_zasel-srazy|_zasel-srazy-pvz|_dom.key', parameter):
        return 'Ключи в '
    elif re.search(r'_mbl|_dom.mbl-key|_2mbl|_dom.mbl', parameter):
        return 'С мебелью'
    elif re.search(r'_kuxn', parameter):
        return 'С кухней'
    elif re.search(r'_kv.otdel', parameter):
        return 'С отделкой'
    elif re.search(r'_ap.park|_ap.dt.sad', parameter):
        return 'Рядом с'
    elif re.search(r'_dom.dod|_dod|_1-11-klass|_curriculum|_personal-plan|_20students|_private-educ|_invitation|_school-present', parameter):
        return 'Самолетум'
    elif re.search(r'_dobavim|_mbl.gift|_gifts', parameter):
        return 'Подарки'
    elif re.search(r'_dom.home-appl-sale|_sale|_flash|_sale-y-par', parameter):
        return 'Скидка'
    elif re.search(r'_rassr|_dom.mbl-rassr', parameter):
        return 'Рассрочка'
    elif re.search(r'_kv-life-vgd|_vgd', parameter):
        return 'Выгода'
    elif re.search(r'_dom.dt.sad|_sch-2dt.sad|_sch-dt.sad', parameter):
        return 'Детский сад и Школа'
    elif re.search(r'_prest-area|_forest-zal|_reka-view|_reka|_dom.water|_kv.centr|_kv.krml|_b.centr|_kv.b.centr|_fin.zal|_city.infr|_beach|_sadovoe|_izhs|_izhs-safety|_izhs-calm', parameter):
        return 'ГЕО'
    elif re.search(r'_cashback-travel|_cshbck-tbank', parameter):
        return 'Кэшбек'
    elif re.search(r'_pvz', parameter):
        return 'Первый взнос'
    elif re.search(r'_bez-pvz|_kv.centr-bez-pvz|_real-bez-pvz|_kv.b.centr-bez-pvz', parameter):
        return 'Без ПВЗ'
    elif re.search(r'_before-after', parameter):
        return 'До-После'
    elif re.search(r'_ready-kv', parameter):
        return 'Готовые квартиры'
    elif re.search(r'_rent-vgd|_rent|_rent-wint', parameter):
        return 'Аренда'
    elif re.search(r'_stud-msk|_prep-sess|_first-kv-own|_hw', parameter):
        return 'Студенты'
    elif re.search(r'_clprt-fast', parameter):
        return 'Целепорт'
    elif re.search(r'_mozh', parameter):
        return 'Можнотека'
    elif re.search(r'_invst', parameter):
        return 'Инвестиции'
    elif re.search(r'_fransh', parameter):
        return 'Франшиза'
    elif re.search(r'_metr', parameter):
        return 'Метр от Самолет'
    elif re.search(r'_trade', parameter):
        return 'trade-in'
    elif re.search(r'_free-reс|_10rec', parameter):
        return 'Рекомендации'
    elif re.search(r'_comfort|_wheel|_zak.dvor|_smart-tech|_home-appl|_terrace|_dom.shale|_private-ter', parameter):
        return 'Продуктовые'
    elif re.search(r'_none', parameter):
        return 'Ничего'
    elif re.search(r'_get-first|_book-fix-cost|_otklad|_save-up-faster|_sp.pur|_choose-now|_nakop', parameter):
        return 'Мотивация'
    elif re.search(r'_kv.wnt2cmback|_paris', parameter):
        return 'Вернуться в квартиру'
    elif re.search(r'_offer|_responsibility|_wishes|_naves-avto|_energy-for-life|_full.life|_mbl-teplo|_mbl-wth|_samokot|_flamingo|_14feb|_sravny|_happy', parameter):
        return 'Другое'
    elif re.search(r'_full-own|_wisk-paws-tail|_transp-cond|_free-meal-c|_free-meal-b', parameter):
        return 'petsflats'
    elif re.search(r'_kv-for-life', parameter):
        return 'Квартиры для жизни'
    elif re.search(r'_kv.metro|_kv.mck|_ap.metro|_kv.mcd|_ap.mck|_ap.mcd|_apart.pyatn.sh|_dom.nov.sh', parameter):
        return 'Транспортная инфраструктура'
    else:
        return 'Unknown'