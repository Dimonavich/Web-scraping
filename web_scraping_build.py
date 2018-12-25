from bs4 import BeautifulSoup
import requests
import csv
from random import choice
import re


def get_data_page(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name =  soup.find('h1', class_='card_title').text.strip()
    except:
        name = ''
    try:
        adress = soup.find('div', class_='info_item').text.strip()
    except:
        adress = ''
    try:
        prices = soup.find('div', class_='descrition_price_item').text.strip().replace(' ', '').replace('\n', '').replace('до', ' до ')
    except:
        prices = ''
        #Price
    try:
        one_room = soup.find('div',  text=re.compile('1-комнатные')).find_next('div').text.strip()
        one_room1 = soup.find('div',  text=re.compile('1-комнатные')).find_next('div').find_next('div').find_next('div').text.strip().replace('\xa0', ' ')    
        one_r = ''.join(one_room1)  + ' ---> ' + ''.join(one_room)
    except:
        one_r = ''
    try:
        two_room = soup.find('div',  text=re.compile('2-комнатные')).find_next('div').text.strip()
        two_room1 = soup.find('div',  text=re.compile('2-комнатные')).find_next('div').find_next('div').find_next('div').text.strip().replace('\xa0', ' ')    
        two_r = ''.join(two_room1)  + ' ---> ' + ''.join(two_room)
    except:
        two_r = ''
    try:
        three_room = soup.find('div',  text=re.compile('3-комнатные')).find_next('div').text.strip()
        three_room1 = soup.find('div',  text=re.compile('3-комнатные')).find_next('div').find_next('div').find_next('div').text.strip().replace('\xa0', ' ')    
        three_r = ''.join(three_room1)  + ' ---> ' + ''.join(three_room)
    except:
        three_r = ''
    try:
        four_room = soup.find('div',  text=re.compile('4-комнатные')).find_next('div').text.strip()
        four_room1 = soup.find('div',  text=re.compile('4-комнатные')).find_next('div').find_next('div').find_next('div').text.strip().replace('\xa0', ' ')    
        four_r = ''.join(four_room1)  + ' ---> ' + ''.join(four_room)
    except:
        four_r = ''
    try:
        multi_room = soup.find('div',  text=re.compile('1-комнатные')).find_next('div').text.strip()
        multi_room1 = soup.find('div',  text=re.compile('1-комнатные')).find_next('div').find_next('div').find_next('div').text.strip().replace('\xa0', ' ')    
        multi_r = ''.join(multi_room1)  + ' ---> ' + ''.join(multi_room)
    except:
        multi_r = ''
    try:
        reg = soup.find('div', text=re.compile('Регион'))
        region=reg.find_parent('div').find_parent('div').find('a').text.strip()
    except:
        region = ''
    try:
        area1 = soup.find('div', text=re.compile('Район'))
        area=area1.find_parent('div').find_parent('div').find('a').text.strip()
    except:
        area = ''
    try:
        loc = soup.find('div', text=re.compile('Локация'))
        location=loc.find_parent('div').find_parent('div').find('a').text.strip()
    except:
        location = ''
    try:
        met = soup.find('div', text=re.compile('Метро'))
        metro=met.find_parent('div').find_parent('div').find('a').text.strip()
    except:
        metro = ''
    try:
        CT = soup.find('div', text=re.compile('Станция МЦК'))
        station=CT.find_parent('div').find_parent('div').find('a').text.strip()
    except:
        station = ''
    try:
        adr = soup.find('div', text=re.compile('Адрес'))
        adres=adr.find_parent('div').find_parent('div').find('div', id='street_novos').text.strip()
    except:
        adres = ''
        # характеристики
    try:
        dev = soup.find('div', text=re.compile('Застройщик'))
        d = dev.find_parent('div').find_parent('div').find_all('a')
        d1 = []
        for i in d:
            d1.append(i.text.strip())
        developer = (', ').join(d1)
    except:
        developer = ''
    try:
        ded = soup.find('div', class_='lh_24 fs_16 fw_m data_card_item', text=re.compile('Срок сдачи'))
        ded1 = ded.find_parent('div').find_parent('div').find_all('div', class_='lh_24 fs_16 d_b data_card_item')
        deadl = []
        for k in ded1:
            deadl.append(k.text.strip().replace('            ', '-').replace('показать еще', ''))
        deadline = (', ').join(deadl).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except:
        deadline = ''
    try:
        type_build = soup.find('div', text=re.compile('Тип здания')).find_next('div').text.strip()
    except:
        type_build = ''
    try:
        floor ='этaжей= ' + soup.find('div', text=re.compile('Этажность')).find_next('div').text.strip()
    except:
        floor = ''
    try:
        ceiling  = 'h= ' + soup.find('div', text=re.compile('Высота потолка')).find_next('div').text.strip()
    except:
        ceiling  = ''
    try:
        fini = soup.find('div', text=re.compile('Отделка')).find_next('div').text.strip()
    except:
        fini = ''
    try:
        park = soup.find('div', text=re.compile('Парковка')).find_next('div').find_all('div', class_='lh_24 fs_16 d_b data_card_item')
        pa = []
        for i in park:
            pa.append(i.text.strip().replace(' ', '').replace('\n', ' '))
        parking = (', ').join(pa)
    except:
        parking = ''
    try:
        rating = 'r= ' + soup.find('div', text=re.compile('Рейтинг')).find_next('div').text.strip()
    except:
        rating = ''
    try:
        stad = soup.find('div', class_='lh_24 fs_16 fw_m data_card_item', text=re.compile('Стадия строительства'))
        st = stad.find_parent('div').find_parent('div').find_all('div', class_='lh_24 fs_16 d_b data_card_item')
        st1 = []
        for s in st:
            st1.append(k.text.strip().replace('            ', '-').replace('показать еще', ''))
        stages = (', ').join(st1).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except:
        stages = ''

    # подробная информация
    try:
        discription = soup.find('div', itemprop='description').get_text().strip().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except:
        discription = ''
    try:
        off_site = soup.find('a', text=re.compile('Официальный сайт')).get('href') 
    except:
        off_site = ''
    #как проехать
    try:
        linee = soup.find('h2', text=re.compile('Как проехать'))
        lin=linee.find_parent('div').text.strip().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except:
        lin = ''
    try:
        inf = soup.find('h2', text=re.compile('Инфраструктура'))
        Infr=inf.find_next_sibling('div').text.strip().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    except:
        Infr = ''
    try:
        koo = soup.find_all('script', type="text/javascript", string=re.compile('ymaps.ready'))
        koo1 = koo[1].get_text("/var coordLong ", strip=True)
        k1 = re.findall('var coordLong = \'[\d\S]+\'', koo1)
        k2 = re.findall('var coordLat = \'[\d\S]+\'', koo1)
        koordinat = k1+k2
    except:
        koordinat = ''


    #где купить 

    try:
        na = soup.find('div', class_='f_s_1 title_hover_item stroke_crop new-sider-title-item adaptive_title_h2').text.strip()
    except:
        na = ''
    try:
        telephon = soup.find('a', class_='va_t mr_10 def_black show-hide-phone').get_text().strip() 
    except:
        telephon = ''
    try:
        tim = soup.find('div', class_='ml_25').get_text().strip()
    except:
        tim = ''

    data = {'name': name,
            'adress': adress,
            'prices': prices,
            'one_r': one_r,
            'two_r': two_r,
            'three_r': three_r,
            'four_r': four_r,
            'multi_r': multi_r,
            'region': region,
            'area': area,
            'location': location,
            'metro': metro,
            'station': station,
            'adres': adres,
            'developer': developer,
            'deadline': deadline,
            'type_build': type_build,
            'floor': floor,
            'ceiling': ceiling,
            'fini': fini,
            'parking': parking,
            'rating': rating,
            'stages': stages,
            'discription': discription,
            'off_site': off_site,
            'lin': lin,
            'Infr': Infr,
            'koordinat': koordinat,
            'na': na,
            'telephon': telephon,
            'tim': tim}
    writer_csv(data)
    return data


def writer_csv(data):
    with open('build.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter = '|')
        writer.writerow((data['name'],
                         data['adress'],
                         data['prices'],
                         data['one_r'],
                         data['two_r'],
                         data['three_r'],
                         data['four_r'],
                         data['multi_r'],
                         data['region'],
                         data['area'],
                         data['location'],
                         data['metro'],
                         data['station'],
                         data['adres'],
                         data['developer'],
                         data['deadline'],
                         data['type_build'],
                         data['floor'],
                         data['ceiling'],
                         data['fini'],
                         data['parking'],
                         data['rating'],
                         data['stages'],
                         data['discription'],
                         data['off_site'],
                         data['lin'],
                         data['Infr'],
                         data['koordinat'],
                         data['na'],
                         data['telephon'],
                         data['tim']))
        print(data['name'], 'parsed')


def main():
    useragents = open('useragents.txt').read().split('\n') 
    proxies = open('proxilist.txt').read().split('\n')
    proxy = {'http': 'http://' + choice(proxies)}
    useragent = {'User-Agent': choice(useragents)}
    filename = 'D:/Selenium/link_build.txt'
    filer = open(filename)
    for i in range(1, 20):
       url ='http://'+ filer.readline().strip() 
       html = requests.get(url, headers=useragent, proxies=proxy).text
       get_data_page(html)


if __name__ == '__main__':
    main()
