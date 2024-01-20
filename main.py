"""
Development: uvicorn main:app --reload
Production: uvicorn main:app --host 0.0.0.0 --port 10000
Folium TileLayers: http://maps.stamen.com
FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
Add city: /add/city
Delete city: /delete/city
"""

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from map import create_map, get_coordinates
from config import AIRTABLE

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/')
async def read_root(q: str = 'watercolor'):
    data = load_data()
    html = create_map(data, q)
    html = add_extra_html_to_head(html)
    return HTMLResponse(content=html, status_code=200)


@app.get('/japan')
async def read_root():
    return FileResponse('static/japan.html')


@app.get('/add/{city}')
async def receive_name(city: str):
    data = load_data()
    if capitalize(city) not in data.keys():
        coordinates = get_coordinates(city)
        if coordinates:
            AIRTABLE.insert({'City': capitalize(city)} | coordinates)
    return RedirectResponse(url='/')


@app.get('/delete/{city}')
async def receive_name(city: str):
    records = AIRTABLE.get_all()
    for r in records:
        if r['fields']['City'] == capitalize(city):
            AIRTABLE.delete(r['id'])
            break
    return RedirectResponse(url='/')


def load_data():
    records = AIRTABLE.get_all()
    fields = [r['fields'] for r in records]
    d = {}
    for field in fields:
        d[field['City']] = {'lat': field['Latitude'], 'lon': field['Longitude']}
    return d


def add_extra_html_to_head(html):
    extra_html = '''
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    '''
    html = html.replace('</head>', f'{extra_html}</head>')
    return html


def capitalize(s):
    return ' '.join([w.title() for w in s.split()])
