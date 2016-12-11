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


def get_number_per_island(game, id_island, id_aircraft, id_city):
    number = 100
    number = number - id_aircraft.distance(id_island)
    number = number - game.distance(id_city, id_island)
    number = number - (get_enemy_pirates_in_range(2, id_island) * 10)
    if get_enemy_pirates_in_range(2, id_island) >= 3:
        return -100
    return number
    pass


def get_list_priority(game, id_aircraft, id_city):
    l = [get_number_per_island(game, game.get_all_islands[0], id_aircraft, id_city),
         get_number_per_island(game, game.get_all_islands[1], id_aircraft, id_city),
         get_number_per_island(game, game.get_all_islands[2], id_aircraft, id_city),
         get_number_per_island(game, game.get_all_islands[3], id_aircraft, id_city)]
    return l
    pass
