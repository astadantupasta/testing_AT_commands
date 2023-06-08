# Import
from at_command import AtCommand
from modules import flags_handling
from modules import read_json
from modules import print_to_file
from modules import print_to_terminal
from at_commands_container import AtCommandsContainer
from serial_communication import SerialCommunication

def main(flag_device_name, flags_port):
    # Read data from a file and append to a list of AtCommands objects
    file_data = read_json.read_data_from_json("at_commands.json", flag_device_name)

    # Initiate container of AtCommands
    at_commands = AtCommandsContainer(file_data)

    # Initiate SerialCommunication object
    serial = SerialCommunication(flags_port)
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

    main(flags.name.upper(), flags.port)


    