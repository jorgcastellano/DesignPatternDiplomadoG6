import abc
import json

class IMap(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def draw(self, data):
        pass


class GeoJsonMap(IMap):
    def draw(self, data):
        return "Dibujando Mapa con formato GeoJson: " + data


class KmlMap:
    def render(self, data):
        return ["Dibujando Mapa con formato KML", data]


class MapToKmlAdapter(IMap):
    def __init__(self):
        self.kml_obj = KmlMap()
    def draw(self, data_json):
        data_kml = self.convert(data_json)
        return self.kml_obj.render(data_kml)

    def convert(self, data):
        return json.loads(data)


class Library:
    def set_data(self, data):
        self.data = data

    def getMap(self):
        # map = GeoJsonMap()
        map = MapToKmlAdapter()
        data = map.draw(self.data)
        print(data)

client = Library()
client.set_data('[{"a": "1", "b": "2"}]')
client.getMap()
