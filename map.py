import folium
from folium.plugins import Fullscreen, MousePosition
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'http://google.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
}


def create_map(data, q):
    style = 'watercolor' if q != 'terrain' else q
    suffix = '' if q != 'terrain' else '{r}'
    f = folium.Figure()
    m = folium.Map(zoom_control=False, location=[40, 0], zoom_start=3).add_to(f)
    folium.TileLayer('https://tiles.stadiamaps.com/tiles/stamen_' + style + '/{z}/{x}/{y}' + suffix + '.jpg',
                     attr='©Fuchs').add_to(m)

    # Add extra HTML
    extra_html = '''
        <script>
            document.addEventListener("keypress", function(event) {
                if (event.keyCode === 32) {  // space bar
                    if (window.location.href.split('?').length == 2) {
                        window.location.href = "/";
                    } else {
                        window.location.href = "/?q=terrain";
                    }
                }
            });
        </script>
    '''
    m.get_root().html.add_child(folium.Element(extra_html))

    # Add Markers
    for k, v in data.items():
        icon = folium.Icon(
            color='purple',
            icon='location-pin',
            prefix='fa'
        )
        folium.Marker(
            location=[v['lat'], v['lon']],
            popup=f'<span style="font-size: 16px">{k}</span>',
            icon=icon
        ).add_to(m)

    if q == 'terrain':
        MousePosition(
            position='topright',
            separator=' | ',
            prefix='Coordinates:',
            num_digits=3,
        ).add_to(m)

    Fullscreen().add_to(m)  # full-screen option
    return m.get_root().render()


def get_coordinates(city):
    base_url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': city,
        'format': 'json',
        'limit': 1
    }
    response = requests.get(base_url, params=params, headers=HEADERS)
    data = response.json()
    if data:
        return {'Latitude': float(data[0]['lat']), 'Longitude': float(data[0]['lon'])}
