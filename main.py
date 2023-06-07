# Import
from at_commands import AtCommands
from modules import flags_handling
from modules import read_json
from modules import at_commands_container_handling

def main(flag_device_name):
    # Read data from a file and append to a list of AtCommands objects
    file_data = read_json.read_data_from_json("at_commands.json", flag_device_name)
    at_commands = at_commands_container_handling.dict_to_list_of_objects(file_data)
    