from Resources.LocationClass import Location
from Resources.Pirates import PirateGame


def get_danger_level(game, location):
    """

    :param location: location of point
    :type location: Location
    :type game: PirateGame
    :return: danger level of given point
    """

    danger = 0
    for enemy in game.get_enemy_living_pirates():
        danger += enemy.distance(location)
    return danger


def get_enemies_in_range(game, radius, location):
    enemies_in_range = []
    for enemy in game.get_enemy_living_pirates():
        if enemy.distance(location) < radius:
            enemies_in_range.append(enemy)

    return enemies_in_range


def route_danger(game, route, pirate):
    """

    :param game: game object
    :type game: PirateGame
    :param route: list of points
    :type route: list
    :param pirate:
    :return:
    """
    final_danger = 0
    for location_tuple in enumerate(route):
        danger = get_danger_level(game, location_tuple[1])
        danger_distance = danger * (0.8 ** location_tuple[0])
        final_danger += danger_distance

    return final_danger
