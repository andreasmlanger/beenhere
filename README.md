# BeenHere

## Introduction
BeenHere is a nimble FastAPI project designed to showcase a Folium map of the world. The application allows users to mark destinations they have visited by leveraging the '/add/{city}' route, and destinations can be removed through the '/delete/{city}' route. Additionally, users can toggle between an artistic watercolor style and a terrain style by simply pressing the SPACE key. Added cities are stored remotely in an AirTable.

### Features
- Interactive Map: Utilizes Folium to provide an interactive and visually appealing map of the world.
- Destination Management: Users can dynamically add and remove destinations by interacting with the '/add/{city}' and '/delete/{city}' routes.
- Visual Styles: Enhances user experience with the ability to switch between an artistic watercolor style and a terrain style by pressing the SPACE key.

### Dependencies
- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- Folium: A Python wrapper for Leaflet.js, allowing the creation of interactive maps in Python.

## License:
This project is licensed under the MIT License.

## Acknowledgments
Thanks to the FastAPI and Folium communities for their excellent frameworks.

Happy exploring with BeenHere! 🌍✈️
