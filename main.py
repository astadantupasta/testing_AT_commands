# Import
from modules.at_command import AtCommand
from modules import flags_handling
from modules import read_json
from modules import print_to_file
from modules import print_to_terminal
from modules import preparation
from modules.at_commands_container import AtCommandsContainer
from modules.serial_communication import SerialCommunication

def main(flags):
    # Extract values from the flags
    flag_device_name = flags.name.upper()
    flags_port = flags.port
    flags_possible_port = flags.possibleport

    # Prepare for the test
    preparation.kill_modem_manager()

    # Read data from a file and append to a list of AtCommands objects
    file_data = read_json.read_data_from_json("at_commands.json", flag_device_name)

    # Initiate container of AtCommands
    at_commands = AtCommandsContainer(file_data)

    # Initiate SerialCommunication object
    serial = SerialCommunication(flags_port, flags_possible_port)
    serial.open_port()

    # Send AT commands to the device
    at_commands.set_at_commands_responses(serial)
    at_commands.set_modem_manufacturer(serial)
    at_commands.set_modem_model(serial)
    serial.close_port()

    # Check if the tests were passed
    at_commands.check_if_tests_are_passed()

    # Print results to terminal and to the CSV file
    print_to_terminal.print_to_terminal(flag_device_name, at_commands)
    print_to_file.print_to_csv(flag_device_name, at_commands)

if __name__ == "__main__":
    flags = flags_handling.get_flags()
    main(flags)


    