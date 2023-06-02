from opganization import Organization
from insurance_company import Insurance_Company
from ShipbuilC import ShipbuilC
from factory import Factory

company_insur =Insurance_Company('"Рога та Копита"','страхування','Пубкін В.В.','Лавренко М.В.',12,'+380963804022','Україна Дніпропетровська обл. м.Кривий Ріг вул. Леоніда Бородича 17','randk@ukr.net',['страхування життя','автостахування'])
company_insur.show_info()
company_insur.add_insurance_policy('страхування майна')
company_insur.show_info()
print('-----------------------------------------------------------------------')

factory_concrete_structures =Factory('ТОВ "ЗБК"','виготовлення залізобетонних конструкцій','Семирядько В.П','Ахметова Р.А.',150,'+38099345678','Україна Дніпропетровська обл. м.Кривий Ріг вул. Переверзева 7','gbk@com.ua',['бетоне кільце','огорожа','бетона стіна'])
factory_concrete_structures.show_info()
factory_concrete_structures.hiring_for_a_job(4)
factory_concrete_structures.show_info()
factory_concrete_structures.dismissal_for_a_job(25)
factory_concrete_structures.show_info()
print('-----------------------------------------------------------------------')

ship_factor1 = ShipbuilC('ТОВ "ВСУ"','будівництво військових кораблів','Потапенко Ф.П','Тягнирядно М.М.',450,'+38093745678','Україна Миколаївська обл. м.Миколаїв вул. Річкова 25','vsu@i.ua','корвети, есмінці, підводні човни ',3)
ship_factor1.show_info()

ship_factor2 = ShipbuilC(' ЗАТ "Мрія"','будівництво сухогрузів','Шрамко Ф.Г.','Шевченко Т.П.',350,'+38093747878','Україна Одеська обл. м.Одеса вул. Портова 14','mria@i.ua','сухогрузи ',2)
ship_factor2.show_info()
print('ship builder company 1 > ship builder company 2 is',ship_factor1 > ship_factor2)
print('ship builder company 1 < ship builder company 2 is',ship_factor1 < ship_factor2)
print('ship builder company 1 >= ship builder company 2 is',ship_factor1 >= ship_factor2)
print('ship builder company 1 <= ship builder company 2 is',ship_factor1 <= ship_factor2)