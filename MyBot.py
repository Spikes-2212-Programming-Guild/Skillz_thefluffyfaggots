import Functions
def do_turn(game):
    for pirate in game.get_my_living_pirates():
        # Get the first island
        destination = game.get_all_islands()[0]
        # Get the sail options to the island
        sail_options = game.get_sail_options(pirate, destination)
        # Set sail!
        game.set_sail(pirate, sail_options[0])
        # Print a message
        game.debug('pirate ' + str(pirate) + ' sails to ' + str(sail_options[0]) + 'sail danger' + Functions.route_danger(game, sail_options))