import re

def is_none(value):
    if value is None:
        return ''
    else:
        return value.lower()


import re


def determine_source(string_param):
    string_param = is_none(string_param)
    patterns = {
        r'((atommedia).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(atommedia))': 'Atommedia',
        r'((aurumrealty).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(aurumrealty))': 'AurumRealty',
        r'((call(.|)of(.|)leads).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(call(.|)of(.|)leads))': 'Call of Leads',
        r'((call(.|)exchange).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(call(.|)exchange))': 'Callexchange',
        r'((callrealty).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(callrealty))': 'CallRealty',
        r'((calltact).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(calltact))': 'CallTact',
        r'((calltobuy).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(calltobuy))': 'Calltobuy',
        r'((cpaexchange).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(cpaexchange))': 'CPAexchange',
        r'((datacon).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(datacon))': 'Datacon',
        r'((datavision).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(datavision))': 'DataVision',
        r'((dmp(.|)one).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(dmp(.|)one))': 'DMP.ONE',
        r'flatoutlet': 'FlatOutlet',
        r'((getflat).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(getflat))': 'GetFlat',
        r'((gidmarket).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(gidmarket))': 'GidMarket',
        r'((i(.|)brand).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(i(.|)brand))': 'I-Brand',
        r'((imetik).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(imetik))': 'iMetik',
        r'((knam).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(knam))': 'KNAM',
        r'((knowhow).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(knowhow))': 'KnowHow',
        r'((kupikvartiru).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(kupikvartiru))': 'Kupikvartiru',
        r'((kvalto).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(kvalto))': 'Kvalto',
        r'((lead(i|l)deal).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(lead(i|l)deal))': 'LeadIdeal',
        r'((like(.|)estate).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(like(.|)estate))': 'Like.Estate',
        r'((madtec).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(madtec))': 'Madtec',
        r'((makeleads).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(makeleads))': 'MakeLeads',
        r'((maketrue).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(maketrue))': 'MakeTrue',
        r'((mapestate).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(mapestate))': 'MapEstate',
        r'((market(.|)(c|с)all).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(market(.|)(c|с)all))': 'MarketCall',
        r'((media(.|)take).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(media(.|)take))': 'Media Take',
        r'((millennium(.|)city).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(millennium(.|)city))': 'Millennium-city',
        r'((mobx).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(mobx))': 'MobX',
        r'monkey': 'Monkey',
        r'((netgrowthlab).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(netgrowthlab))': 'NetGrowthLab',
        r'((otclick).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(otclick))': 'Otclick',
        r'((ox(.|)capital).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(ox(.|)capital))': 'OX Capital',
        r'((partners).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(partners))': 'Partners',
        r'((pointcall).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(pointcall))': 'PointCall',
        r'((premium(.|)id).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(premium(.|)id))': 'Premium ID',
        r'((profiledata).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(profiledata))': 'ProfileDATA',
        r'((reffection).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(reffection))': 'Reffection',
        r'((reforum).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(reforum))': 'Reforum',
        r'((ro(c|)ket(.|)ad).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(ro(c|)ket(.|)ad))': 'RocketAd',
        r'roombe(rr|r)y|румбе(рр|р)и': 'Roomberry',
        r'((rosttech).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(rosttech))': 'Rosttech',
        r'((sellmore).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(sellmore))': 'SellMore',
        r'((solutions(.|)pro).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(solutions(.|)pro))': 'Solutions Pro',
        r'((southmedia).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(southmedia))': 'Southmedia',
        r'((stroynov).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(stroynov))': 'Stroynov',
        r'((telegram(.|)nearby).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(telegram(.|)nearby))': 'Telegram Nearby',
        r'((unity).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(unity))': 'Unity',
        r'((uzhedoma).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(uzhedoma))': 'Uzhedoma',
        r'((wantresult).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(wantresult))': 'WantResult',
        r'((yugo).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(yugo))': 'YUGO'
    }

    for pattern, placement in patterns.items():
        if re.search(pattern, string_param, re.IGNORECASE):
            return placement

    return 'Not Found'


