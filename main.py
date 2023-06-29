# Import
from modules.at_command import AtCommand
from modules import flags_handling
from modules import read_json
from modules import print_to_file
from modules import print_to_terminal
from modules import shell_commands
from modules.at_commands_container import AtCommandsContainer
from modules.serial_communication import SerialCommunication
from os import system
import importlib

def main(args):
    # Extract communication arguments from the flags
    flag_device_name, first_arg, second_arg, third_arg = flags_handling.get_communication_arguments(args)

    # Prepare for the test
    shell_commands.disable_process()

    # Read data from a file and append to a list of AtCommands objects
    file_data = read_json.read_data_from_json("at_commands.json", flag_device_name)

    # Initiate container of AtCommands
    at_commands = AtCommandsContainer(file_data)

    # Dynamically import module and class
    mod = importlib.import_module(f'modules.{at_commands.get_module()}')
    Communication = getattr(mod, at_commands.get_class())

    # Initiate object for communication
    comm = Communication(first_arg, second_arg, third_arg)
    comm.open_port()

    # Send AT commands to the device
    at_commands.set_modem_manufacturer(comm)
    at_commands.set_modem_model(comm)
    at_commands.set_at_commands_responses(comm, flag_device_name)
    
    comm.close_port()

    # Check if the tests were passed
    at_commands.check_if_tests_are_passed()

    # Print results  to the CSV file
    print_to_file.print_to_csv(flag_device_name, at_commands)

if __name__ == "__main__":
    flags = flags_handling.get_flags()
    flags_handling.test_flags(flags)
    while True:
        main(flags)


    