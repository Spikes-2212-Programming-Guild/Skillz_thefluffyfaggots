from Resources.PirateClass import BasePirate
from Resources.PlayerClass import BasePlayer
from Resources.DroneClass import BaseDrone
from Resources.IslandClass import BaseIsland
from Resources.CityClass import BaseCity
from Resources.LocationClass import Location
from Resources.Aircraft import Aircraft
from Resources.MapObject import MapObject
from Resources.GameObject import GameObject


def get_danger_level(location):
    pass


def get_enemy_pirates_in_range(randius, location):
    pass


def get_number_per_island(game, id_island,id_aircraft,id_city):
    number = 100
    number = number - id_aircraft.distance(id_island)
    number = number - game.distance(id_city, id_island)
    number = number - (get_enemy_pirates_in_range(2, id_island) * 10)
    if get_enemy_pirates_in_range(2, id_island):
        return 0
    return number
    pass

