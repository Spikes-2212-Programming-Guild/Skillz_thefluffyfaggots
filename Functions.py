from Resources.PirateClass import BasePirate
from Resources.PlayerClass import BasePlayer
from Resources.DroneClass import BaseDrone
from Resources.IslandClass import BaseIsland
from Resources.CityClass import BaseCity
from Resources.LocationClass import Location
from Resources.Aircraft import Aircraft
from Resources.MapObject import MapObject
from Resources.GameObject import GameObject
from Resources.Pirates import PirateGame


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

def get_friendly_pirates_in_range(game,radius, location):
    """
    :param game:
    :type game:PirateGame
    :param radius:
    :type radius:int
    :param location:
    :type location:Location
    :return: list
    """
    friends_in_range = []
    for aircraft in game.get_my_living_pirates():
        if aircraft.distance(location) < radius:
            friends_in_range.append(aircraft)

    return friends_in_range



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
    number -= ((len(get_enemy_pirates_in_range(2, island_object.get_location))-(len(get_friendly_pirates_in_range(game,2,island_object.get_location())))) * 10)
    if len(get_enemy_pirates_in_range(2, island_object)) >= 3:
        return -100
    return number


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
    game.get_attack_range()
    l = [get_number_per_island(game, game.get_all_islands[0], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[1], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[2], aircraft_object, city_object),
         get_number_per_island(game, game.get_all_islands[3], aircraft_object, city_object)]
    return l


