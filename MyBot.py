from Resources.Pirates import *

def sortIslands(game):
    """
            :param game:
            :type game: PirateGame
            :return: None
    """
    islands = game.get_all_islands()
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range (1, len(islands)):
            game.debug("island index = " + str(i))
            if game.get_all_islands()[0].distance(islands[i]) < game.get_all_islands()[0].distance(islands[i - 1]):
                isSorted =False
                temp = islands[i]
                islands[i] = islands[i - 1]
                islands[i - 1] = temp
    return islands

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
    islands = sortIslands(game)
    islands = sorted(game.get_all_islands(), key=lambda i: game.get_my_cities()[0].distance(i))
    myPirates = game.get_my_living_pirates()
    group1 = myPirates[ : len(myPirates) / 2]
    group2 = myPirates[len(myPirates) / 2 : ]
    pirateIndex = 0
    for pirate in group1:
        if not bools_Ship_Taken_turn[pirateIndex]:
            sailOption = game.get_sail_options(pirate, islands[0].get_location())[0]
            game.set_sail(pirate, sailOption)
        pirateIndex += 1
    pirateIndex = 0
    for pirate in group2:
        if not bools_Ship_Taken_turn[pirateIndex + len(group2) - 1]:
            sailOption = game.get_sail_options(pirate, islands[1].get_location())[0]
            game.set_sail(pirate, sailOption)
        pirateIndex += 1
    for drone in game.get_my_living_drones():
        sailOption = game.get_sail_options(drone, game.get_my_cities()[0].get_location())[0]
        game.set_sail(drone, sailOption)
