from Resources.LocationClass import Location


def get_danger_level(game, location):
    """

    :param location: location of point
    :type location: Location
    :return: danger level of given point
    """

    danger = 0
    for enemy in game.get_enemy_living_pirates():
        danger += enemy.MapObject.distance(location)
    return danger


def get_enemies_in_range(game, radius, location):
    enemies_in_range = []
    for enemy in game.get_enemy_living_pirates():
        if enemy.distance(location) < radius:
            enemies_in_range.append(enemy)

    return enemies_in_range
