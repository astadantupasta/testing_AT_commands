import csv
from datetime import datetime
from modules.at_commands_container import AtCommandsContainer
from modules.at_command import AtCommand

def get_test_time():
    """Get current time in a string form:
    Y-m-d_HhMmSs.
    :return: current time
    """
    return datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")

def get_file_name(device_name, test_time):
    """Composes a csv file name in a form: router_date_time.csv
    
    :test_time: time of the test
    :router_name: name of the router
    :return: file name 
    """
    if len(device_name) < 5:
        raise("Router name indicated inproperly.")
    
    return "results/" + device_name + '_' + test_time + ".csv"

def print_to_csv(device_name, at_commands):
    """Prints AtCommands' data to a CSV file: device_name,
    date and time of the test, manufacturer and model of the modem,
    commands, expected_response, received_response, test_is_passed.
    
    :device_name: name of the device
    :at_commands: an object of AtCommandsContainer
    """
    test_time = get_test_time()
    file_name = get_file_name(device_name, test_time)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        # Writing device information
        writer.writerow(["Tested device: " + device_name])
        writer.writerow(["Date and time: " + test_time])
        writer.writerow(["Modem manufacturer: " + at_commands.get_modem_manufacturer()])
        writer.writerow(["Modem model: " + at_commands.get_modem_model()])

        # Writing information of the commands
        writer.writerow(["Meaning",
                         "Command",
                         "Expected",
                         "Received",
                         "Passed"])
        
        for at_command in at_commands.yield_at_commands():
            writer.writerow(at_command.get_all_values())


