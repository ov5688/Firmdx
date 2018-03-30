import googlemaps
from HT import GOOGLE_KEY, GOOGLE_DISTANCE_KEY
from servicePr.firm import Firmeneintrag_new
# from operator import itemgetter

geocode = dict()

class GeoCoords:

    def __init__(self):
        self.data = []

    def distance_matrix(self, query, list):
        gmaps = googlemaps.Client(key=GOOGLE_DISTANCE_KEY)
        dist_t = {}
        plz = []

        for l in list:
            distances = gmaps.distance_matrix(str(query) + ", Schweiz", str(l.plz) + ", Schweiz")
            dist_t[l.id] = distances['rows'][0]['elements'][0]['distance']['value']

        dist_t = sorted(dist_t.items(), key=lambda x : int(x[1]), reverse=False)
        return dist_t

    def latLng(self, branche):

        gmaps = googlemaps.Client(key=GOOGLE_DISTANCE_KEY)
        lat = []
        lng = []

        for adress in branche:
            adressen = gmaps.geocode(adress.ort + " " + str(adress.plz))
            lat.append(adressen[0]['geometry']['location']['lat'])
            lng.append(adressen[0]['geometry']['location']['lng'])

        return (lat, lng)

    def getAllGeocoords(self, f):

        firma = Firmeneintrag_new()
        branchen = ('Umzug', 'Reinigung', 'Maler', 'Baufirma', 'Architekt',
                    'Catering', 'Schreiner', 'Gartenbau', 'Immobilien', 'Sanitaer')

        for b in branchen:
            firma_n = firma.getFirm(b, f)

            geo = GeoCoords()
            geocode[b] = geo.latLng(firma_n)

        return geocode

geo = GeoCoords()
