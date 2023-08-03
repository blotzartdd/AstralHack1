from bs4 import BeautifulSoup
import requests
import json

from bs4 import BeautifulSoup
import requests

HEADERS = {'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

all_worker_dict = {}


def parce():
    first_url = 'https://kaluga.hh.ru/search/resume?text=&logic=normal' \
            '&pos=full_text&exp_period=all_time&exp_company_size=' \
            'any&exp_industry=any&specialization=1&area=43&relocation' \
            '=living_or_relocation&salary_from=10000&salary_to=150000&currency_code' \
            '=RUR&education=none&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=' \
            '0&items_on_page=100&no_magic=true'

    req = requests.get(first_url, headers=HEADERS)

    src = req.text

    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(src)

    with open('index.html', encoding='utf-8') as f:
        src = f.read()

    soup = BeautifulSoup(src, 'lxml')

    all_worker_blocks = soup.find(class_='bloko-column bloko-column_s-8'
                                         ' bloko-column_m-9 bloko-column_l-13').find_all(class_='resume-search-item')
    for el in all_worker_blocks:
        work = el.find(class_='resume-search-item__name').text
        work_url = 'https://kaluga.hh.ru' + el.find(class_='resume-search-item__name').get('href')
        payment = el.find(class_='bloko-text bloko-text_large bloko-text_strong').text
        age = el.find(class_='resume-search-item__fullname').find('span')
        work_exp = el.find('div', {'data-qa': 'resume-serp__resume-excpirience-sum'})
        if work_exp:
            work_exp = ' '.join(work_exp.text.split()[0:2])
        work_src = requests.get(work_url, headers=HEADERS).text
        work_soup = BeautifulSoup(work_src, 'lxml')
        sex = work_soup.find('span', {'data-qa': 'resume-personal-gender'}).text
        city = work_soup.find('span', {'data-qa': 'resume-personal-address'}).text
        if age:
            age = age.text
        else:
            age = 'Не указан'
        if not payment:
            payment = 'Договорная'
        payment = payment.replace(' ', ' ')
        payment = payment.replace(' ', '')
        age = age.replace(' ', ' ')
        all_worker_dict[work] = {'Зарплата': payment, 'Возраст': age,
                                 'Пол': sex, 'Опыт работы': work_exp,
                                 'Город': city, 'Ссылка': work_url}
    return all_worker_dict


def result(request):
    parce()
    if not request['Название']:
        return None
    if request['Название'] in all_worker_dict.keys():
        if request['Зарплата']:
            if not (request['Зарплата'][0] <= int(all_worker_dict[request['Название']]['Зарплата']) <= request['Зарплата'][0]):
                return None
        if request['Возраст']:
            if not request['Возраст'] == all_worker_dict[request['Название']]['Возраст']:
                return None
        if request['Пол']:
            if not request['Пол'] == all_worker_dict[request['Название']]['Пол']:
                return None
        if request['Город']:
            if not request['Город'] == all_worker_dict[request['Название']]['Город']:
                return None
        return all_worker_dict[request['Название']]


def save_in_json():
    parce()
    with open('all_workers_dict.json', 'w', encoding='utf-8') as file:
        json.dump(all_worker_dict, file, indent=4, ensure_ascii=False)
