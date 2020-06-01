from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

import datetime as dt
from pprint import pprint
import collections
from settings import PATH_DATA_WINE

def run_wine():
    
    wines = pandas.read_excel(PATH_DATA_WINE)
    wine_list = wines.to_dict(orient = 'record')

    # создаем список вин для каждой категории
    categories = collections.defaultdict(list)
    for wine_data in wine_list:         
        value = (wine_data['Категория'])            
        categories[value].append(wine_data)    
        

    # вычисляем возраст фирмы
    date_born =  dt.date(year=1920, month=1,day=1)
    date_now = dt.date.today()
    company_age = date_now.year - date_born.year


    env = Environment(
        loader = FileSystemLoader('.'),
        autoescape = select_autoescape(['html','xml'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        company_age = company_age, #возраст фирмы
        categories = categories, #категории вин    
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
