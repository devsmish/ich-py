'''1. Создайте класс City, представляющий город с координатами.
У каждого города есть поля name, latitude, longitude.
Добавьте строковое представление объекта.
Добавьте метод distance(city1, city2), который возвращает кортеж (latitude, longitude) между двумя городами.
Проверьте расстояние между двумя городами.
Пример вывода: 
City: Berlin (52.52, 13.4)
City: Paris (48.85, 2.35)
Distance: 14.72'''
class City:
    def __init__(self, name, latitude, longitute):
        self.name = name
        self.latitude = latitude
        self.longitute = longitute

    @staticmethod
    def distance(city1, city2):
        return round(city1.latitude - city2.latitude, 6), round(city1.longitute - city2.longitute, 6)

    def __str__(self):
        return f"{self.name}: {self.latitude}, {self.longitute}"

city1 = City('Berlin', 52.52, 13.4)
city2 = City('Paris', 48.85, 2.35)

print(City.distance(city1, city2))

'''2. Доработайте класс City.
Добавьте метод from_string(data), который создаёт объект из строки вида "Rome:41.89,12.51".
Проверьте создание нового объекта через этот метод и выведите его.
Пример вывода:
City: Rome (41.89, 12.51)'''
class City:
    def __init__(self, name, latitude, longitute):
        self.name = name
        self.latitude = latitude
        self.longitute = longitute

    @classmethod
    def from_string(cls, string_data):
        name, other = string_data.split(':')
        latitude, longtitude = other.split(',')
        return cls(name=name, latitude=latitude, longitute=longtitude)

    @staticmethod
    def distance(city1, city2):
        return round(city1.latitude - city2.latitude, 6), round(city1.longitute - city2.longitute, 6)

    def __str__(self):
        return f"{self.name}: {self.latitude}, {self.longitute}"

city1 = City('Berlin', 52.52, 13.4)
city2 = City('Paris', 48.85, 2.35)

print(City.from_string("Rome:41.89,12.51"))
rome = City.from_string("Rome:41.89,12.51")
print(rome.name)