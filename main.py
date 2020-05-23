from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

import datetime as dt
from pprint import pprint
import collections

wines2 = pandas.read_excel('wine3.xlsx')
cards2 = wines2.to_dict(orient = 'record')

# создаем список вин для каждой категории
category = collections.defaultdict(list)
for i in cards2:   
    key = (i['Категория'])
    category[key].append(i)
pprint(category)

# вычисляем возраст фирмы
date_born =  dt.date(year=1920, month=1,day=1)
date_now = dt.date.today()
date_age = date_now.year - date_born.year


env = Environment(
    loader = FileSystemLoader('.'),
    autoescape = select_autoescape(['html','xml'])
)
template = env.get_template('template.html')

rendered_page = template.render(
    date_text = date_age, #возраст фирмы
    categories = category, #категории вин    
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
