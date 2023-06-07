from at_commands import AtCommands

def dict_to_list_of_objects(data):
    """Returns a list of AtCommands objects,
    converted from dictionary.
    :return: a list of AtCommands objects
    """

    at_commands = []
    for dictionary in data['at_commands']:
        at_commands.append(AtCommands(dictionary))

    return at_commands