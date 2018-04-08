import googlemaps
from HT import GOOGLE_KEY, GOOGLE_DISTANCE_KEY
from servicePr.firm import Firmeneintrag_new
from math import radians, sin, cos, acos

geocode = dict()

class GeoCoords:

    def __init__(self):
        self.data = []

    #https://www.w3resource.com/python-exercises/math/python-math-exercise-27.php
    def get_distance(self, search_input, geocode, list):

        i = 0
        dist = []
        gmaps = googlemaps.Client(key=GOOGLE_DISTANCE_KEY)
        lat, lng = geocode

        start_point = gmaps.geocode(search_input + ", Schweiz")
        start_point_lat = radians(float(start_point[0]['geometry']['location']['lat']))
        start_point_lng = radians(float(start_point[0]['geometry']['location']['lng']))

        for l in lng:
            end_point_lng = radians(float(l))
            end_point_lat = radians(float(lat[i]))
            dist.append(int(6371.01 * acos(sin(start_point_lat)*sin(end_point_lat) + cos(start_point_lat)*cos(end_point_lat)*cos(start_point_lng - end_point_lng))))
            i=i+1

        return dist

    def distance_matrix(self, query, list):
        gmaps = googlemaps.Client(key=GOOGLE_DISTANCE_KEY)

        dist = {}
        plz = []

        for l in list:
            distances = gmaps.distance_matrix(str(query) + ", Schweiz", str(l.plz) + ", Schweiz")
            dist[l.id] = distances['rows'][0]['elements'][0]['distance']['value']

        dist = sorted(dist.items(), key=lambda x : int(x[1]), reverse=False)

        return dist

    def latLng(self, list):

        gmaps = googlemaps.Client(key=GOOGLE_DISTANCE_KEY)
        lat = []
        lng = []
        id = []

        for adress in list:
            adressen = gmaps.geocode(adress.ort + " " + str(adress.plz))
            lat.append(adressen[0]['geometry']['location']['lat'])
            lng.append(adressen[0]['geometry']['location']['lng'])
            id.append(adress.id)

        return (lat, lng, id)

    def getAllGeocoords(self, f):

        firma = Firmeneintrag_new()
        branchen = ('Umzug', 'Reinigung', 'Maler', 'Baufirma', 'Architekt',
                    'Catering', 'Schreiner', 'Gartenbau', 'Immobilien', 'Sanitaer')

        for b in branchen:
            firma_n = firma.getFirm(b, f)
            geo = GeoCoords()
            geocode[b] = self.latLng(firma_n)

        return geocode

geo = GeoCoords()
