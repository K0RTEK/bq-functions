CASE 
          -- `donstroy-analytics.cook_procedures.get_cpa`(
          -- CONCAT(
          --   IFNULL(calltracking,""),"_",
          --   IFNULL(utm_source,""),"_",
          --   IFNULL(utm_medium,""),"_",
          --   IFNULL(utm_campaign,""),"_",
          --   IFNULL(utm_content,""),"_",
          --   IFNULL(utm_term,"")))
            WHEN REGEXP_CONTAINS(string_param,r'((atommedia).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(atommedia))') 
              THEN 'Atommedia'

            WHEN REGEXP_CONTAINS(string_param,r'((aurumrealty).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(aurumrealty))') 
              THEN 'AurumRealty'

            WHEN REGEXP_CONTAINS(string_param,r'((call(.|)of(.|)leads).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(call(.|)of(.|)leads))') 
              THEN 'Call of Leads'

            WHEN REGEXP_CONTAINS(string_param,r'((call(.|)exchange).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(call(.|)exchange))') 
              THEN 'Callexchange'

            WHEN REGEXP_CONTAINS(string_param,r'((callrealty).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(callrealty))') 
              THEN 'CallRealty'

            WHEN REGEXP_CONTAINS(string_param,r'((calltact).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(calltact))') 
              THEN 'CallTact'

            WHEN REGEXP_CONTAINS(string_param,r'((calltobuy).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(calltobuy))') 
              THEN 'Calltobuy'

            WHEN REGEXP_CONTAINS(string_param,r'((cpaexchange).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(cpaexchange))') 
              THEN 'CPAexchange'

            WHEN REGEXP_CONTAINS(string_param,r'((datacon).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(datacon))') 
              THEN 'Datacon'

            WHEN REGEXP_CONTAINS(string_param,r'((datavision).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(datavision))') 
              THEN 'DataVision'

            WHEN REGEXP_CONTAINS(string_param,r'((dmp(.|)one).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(dmp(.|)one))') 
              THEN 'DMP.ONE'

            WHEN REGEXP_CONTAINS(string_param,r'flatoutlet') 
              THEN 'FlatOutlet'

            WHEN REGEXP_CONTAINS(string_param,r'((getflat).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(getflat))') 
              THEN 'GetFlat'

            WHEN REGEXP_CONTAINS(string_param,r'((gidmarket).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(gidmarket))') 
              THEN 'GidMarket'

            WHEN REGEXP_CONTAINS(string_param,r'((i(.|)brand).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(i(.|)brand))') 
              THEN 'I-Brand'

            WHEN REGEXP_CONTAINS(string_param,r'((imetik).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(imetik))') 
              THEN 'iMetik'

            WHEN REGEXP_CONTAINS(string_param,r'((knam).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(knam))') 
              THEN 'KNAM'

            WHEN REGEXP_CONTAINS(string_param,r'((knowhow).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(knowhow))') 
              THEN 'KnowHow'

            WHEN REGEXP_CONTAINS(string_param,r'((kupikvartiru).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(kupikvartiru))') 
              THEN 'Kupikvartiru'

            WHEN REGEXP_CONTAINS(string_param,r'((kvalto).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(kvalto))') 
              THEN 'Kvalto'

            WHEN REGEXP_CONTAINS(string_param,r'((lead(i|l)deal).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(lead(i|l)deal))') 
              THEN 'LeadIdeal'

            WHEN REGEXP_CONTAINS(string_param,r'((like(.|)estate).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(like(.|)estate))') 
              THEN 'Like.Estate'

            WHEN REGEXP_CONTAINS(string_param,r'((madtec).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(madtec))') 
              THEN 'Madtec'

            WHEN REGEXP_CONTAINS(string_param,r'((makeleads).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(makeleads))') 
              THEN 'MakeLeads'

            WHEN REGEXP_CONTAINS(string_param,r'((maketrue).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(maketrue))') 
              THEN 'MakeTrue'

            WHEN REGEXP_CONTAINS(string_param,r'((mapestate).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(mapestate))') 
              THEN 'MapEstate'

            WHEN REGEXP_CONTAINS(string_param,r'((market(.|)(c|с)all).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(market(.|)(c|с)all))') 
              THEN 'MarketCall'

            WHEN REGEXP_CONTAINS(string_param,r'((media(.|)take).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(media(.|)take))') 
              THEN 'Media Take'

            WHEN REGEXP_CONTAINS(string_param,r'((millennium(.|)city).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(millennium(.|)city))') 
              THEN 'Millennium-city'

            WHEN REGEXP_CONTAINS(string_param,r'((mobx).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(mobx))') 
              THEN 'MobX'

            WHEN REGEXP_CONTAINS(string_param,r'monkey') 
              THEN 'Monkey'

            WHEN REGEXP_CONTAINS(string_param,r'((netgrowthlab).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(netgrowthlab))') 
              THEN 'NetGrowthLab'

            WHEN REGEXP_CONTAINS(string_param,r'((otclick).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(otclick))') 
              THEN 'Otclick'

            WHEN REGEXP_CONTAINS(string_param,r'((ox(.|)capital).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(ox(.|)capital))') 
              THEN 'OX Capital'

            WHEN REGEXP_CONTAINS(string_param,r'((partners).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(partners))') 
              THEN 'Partners'

            WHEN REGEXP_CONTAINS(string_param,r'((pointcall).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(pointcall))') 
              THEN 'PointCall'

            WHEN REGEXP_CONTAINS(string_param,r'((premium(.|)id).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(premium(.|)id))') 
              THEN 'Premium ID'

            WHEN REGEXP_CONTAINS(string_param,r'((profiledata).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(profiledata))') 
              THEN 'ProfileDATA'

            WHEN REGEXP_CONTAINS(string_param,r'((reffection).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(reffection))') 
              THEN 'Reffection'

            WHEN REGEXP_CONTAINS(string_param,r'((reforum).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(reforum))') 
              THEN 'Reforum'

            WHEN REGEXP_CONTAINS(string_param,r'((ro(c|)ket(.|)ad).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(ro(c|)ket(.|)ad))') 
              THEN 'RocketAd'

            WHEN REGEXP_CONTAINS(string_param,r'roombe(rr|r)y|румбе(рр|р)и') 
              THEN 'Roomberry'

            WHEN REGEXP_CONTAINS(string_param,r'((rosttech).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(rosttech))') 
              THEN 'Rosttech'

            WHEN REGEXP_CONTAINS(string_param,r'((sellmore).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(sellmore))') 
              THEN 'SellMore'

            WHEN REGEXP_CONTAINS(string_param,r'((solutions(.|)pro).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(solutions(.|)pro))') 
              THEN 'Solutions Pro'

            WHEN REGEXP_CONTAINS(string_param,r'((southmedia).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(southmedia))') 
              THEN 'Southmedia'

            WHEN REGEXP_CONTAINS(string_param,r'((stroynov).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(stroynov))') 
              THEN 'Stroynov'

            WHEN REGEXP_CONTAINS(string_param,r'((telegram(.|)nearby).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(telegram(.|)nearby))') 
              THEN 'Telegram Nearby'

            WHEN REGEXP_CONTAINS(string_param,r'((unity).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(unity))') 
              THEN 'Unity'

            WHEN REGEXP_CONTAINS(string_param,r'((uzhedoma).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(uzhedoma))') 
              THEN 'Uzhedoma'

            WHEN REGEXP_CONTAINS(string_param,r'((wantresult).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(wantresult))') 
              THEN 'WantResult'

            WHEN REGEXP_CONTAINS(string_param,r'((yugo).*(call|cpa|лидоген|звон|fid))|((call|cpa|лидоген|звон|fid).*(yugo))') 
              THEN 'YUGO'

          END