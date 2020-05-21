from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas

import datetime as dt

wine_ex = pandas.read_excel('wine.xlsx')
print(wine_ex.to_dict(orient='record'))

env = Environment(
    loader = FileSystemLoader('.'),
    autoescape = select_autoescape(['html','xml'])
)
template = env.get_template('template.html')

date_born =  dt.date(year=1920, month=1,day=1)
date_now = dt.date.today()
date_age = date_now.year - date_born.year

rendered_page = template.render(
    date_text = date_age

)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
