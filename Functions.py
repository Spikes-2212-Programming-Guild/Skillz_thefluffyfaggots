from Resources.PirateClass import BasePirate
from Resources.PlayerClass import BasePlayer
from Resources.DroneClass import BaseDrone
from Resources.IslandClass import BaseIsland
from Resources.CityClass import BaseCity
from Resources.LocationClass import Location
from Resources.Aircraft import Aircraft
from Resources.MapObject import MapObject
from Resources.GameObject import GameObject


def get_danger_level(locations, id_aircraft):
    locations[0]
    pass


def get_enemy_pirates_in_range(randius, location):
    """

    :param randius:
    :param location:
    :type location:iLocaton
    :return: int
    """
    pass


def get_number_per_island(game, island_object, aircraft_object, city_object):
    """

    :param game:
    :type game:PirateGame
    :param island_object:
    :type island_object:GameObject
    :param aircraft_object:
    :type aircraft_object:GameObject
    :param city_object:
    :type city_object:GameObject
    :return:
    """

    number = 100
    number -= aircraft_object.distance(aircraft_object)
    number -= city_object.distance(island_object)
    number -= (len(get_enemy_pirates_in_range(2, island_object.get_location)) * 10)
    if get_enemy_pirates_in_range(2, island_object) >= 3:
        return -100
    return number
    pass


def get_list_priority(game, aircraft_object, city_object):
    """
     :param game:
     :type game:PirateGame
     :param aircraft_object:
     :type aircraft_object:GameObject
     :param city_object:
     :type city_object:GameObject
     :return: List
     """
    l = [get_number_per_island(game, game.get_all_islands[0], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[1], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[2], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[3], aircraft_object, city_object)]
    return l
    pass
