from game import *


def get_closest_island(game):
    """

        :param game:
        :type game: PirateGame
        :type mycity: City
        :return: None
    """
    islands = game.get_all_islands()
    myCity = game.get_my_cities()[0]
    dist = myCity.distance(islands[0])
    result = islands[0]
    for island in islands:
        if myCity.distance(island) < dist:
            result = island
    return result


def init_data(game):
    """
            :param game:
            :type game: PirateGame
            :return: None
    """


def do_turn(game):
    """

    :param game:
    :type game: PirateGame
    :return: None
    """
    bools_Ship_Taken_turn = [False, False, False, False, False]
    pirateIndex = 0
    for pirate in game.get_my_living_pirates():
        for enemy in game.get_enemy_living_aircrafts():
            if pirate.in_attack_range(enemy):
                bools_Ship_Taken_turn[pirateIndex] = True
                game.attack(pirate, enemy)
            else:
                bools_Ship_Taken_turn[pirateIndex] = False
        pirateIndex += 1
    island = get_closest_island(game)

    pirateIndex = 0
    for pirate in game.get_my_living_pirates():
        if not bools_Ship_Taken_turn[pirateIndex]:
            sailOption = game.get_sail_options(pirate, island.get_location())[0]
            game.set_sail(pirate, sailOption)
        pirateIndex += 1

    for drone in game.get_my_living_drones():
        sailOption = game.get_sail_options(drone, game.get_my_cities()[0].get_location())[0]
        game.set_sail(drone, sailOption)
