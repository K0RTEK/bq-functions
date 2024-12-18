### cook_procedures.get_object(parameter)

case
    when regexp_contains(lower(parameter), r'мих|михалковский|mihalkovskij|mihalkov') then 'Михалковский'
    when regexp_contains(lower(parameter), r'вв|варшавские ворота') then 'Варшавские ворота'
    when regexp_contains(lower(parameter), r'пп2|петровский парк 2|petrovskij.park.2') then 'Петровский парк 2'
    when regexp_contains(lower(parameter), r'пп|петровский парк') and not regexp_contains(lower(parameter), r'пп2') then 'Петровский парк'
    when regexp_contains(lower(parameter), r'сп2|семеновский парк 2|семёновский парк 2|semenovskij.park.2') then 'Семеновский парк 2'
    when regexp_contains(lower(parameter), r'сп|семеновский парк|семёновский парк') and not regexp_contains(lower(parameter), r'2') then 'Семеновский парк'
    when regexp_contains(lower(parameter), r'фнв|фн|фонвизинский') then 'Фонвизинский'
    when regexp_contains(lower(parameter), r'блт|бт|балтийский') then 'Балтийский'
    when regexp_contains(lower(parameter), r'окп|октябрьское поле|oktyabrskoe.pole') then 'Октябрьское поле'
    when regexp_contains(lower(parameter), r'ках|каховская') then 'Каховская'
    when regexp_contains(lower(parameter), r'орб|орехово') then 'Орехово-Борисово'
    when regexp_contains(lower(parameter), r'воп|воронцовский парк') then 'Воронцовский парк'
    
    
    else 'Не определено'
    end