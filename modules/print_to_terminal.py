from prettytable import PrettyTable
from os import system, name

def print_data_to_table(at_commands):
    """Prints AtCommand container to table.
    
    :at_commands: AtCommandsContainer object
    """
    t = PrettyTable(['command', 'passed'])

    if at_commands.get_count() == 0:
        raise Exception("modules/print_to_terminal.py: container is empty.")
    
    for at_command in at_commands.yield_at_commands():
        t.add_row([at_command.get_command(),
                    at_command.get_test_is_passed()])
    
    t.align['commad'] = 'l'
    t.align['passed'] = 'l'
    print(t)

def print_to_terminal(device_name, at_commands):
    """Prints required information to the terminal.
    A number of passed tests is marked in gree; not passed - red.
    
    :device_name: name of the device
    :at_commands: AtCommandsContainer object
    """
    CRED = '\033[91m'
    CEND = '\033[0m'
    CGREEN = '\033[92m'

    print_data_to_table(at_commands)
    print("Device name: " + device_name)
    print("Passed tests: " + CGREEN + str(at_commands.count_passed_tests()) + CEND)
    print("Not passed tests: " + CRED + str(at_commands.count_not_passed_tests()) + CEND)
    print("Num of configurations: " + str(at_commands.get_count()))
    print("End of the test!")
    print("\n\n")

def print_one_command(at_command, device_name, at_commands):
    """Prints to terminal results of one AT command and
    summary (number of passed tests in green; not passed -red)

    :at_command: an object of AtCommand
    :device_name: name of the device
    :at_commands: AtCommandsContainer object
    """
    CEND = '\033[0m'
    CRED = '\033[91m'
    CGREEN = '\033[92m'

    test_is_passed = ''
    if at_command.get_test_is_passed(): 
        color = '\033[92m' 
        test_is_passed = 'Passed'
    else: 
        color = '\033[91m'
        test_is_passed = 'Failed'

    print("Command: " + at_command.get_command() + ' '*10)
    print("Response: " + at_command.get_received_response() + ' '*10)
    print("Expected: " + at_command.get_expected_response() + ' '*12)
    print("Passed the test: " + color + test_is_passed + CEND + ' '*12)
    print(' '*20)
    print("Device name: " + device_name + ' '*10)
    print("Passed tests: " + CGREEN + str(at_commands.count_passed_tests()) + CEND + ' '*10)
    print("Failed tests: " + CRED + str(at_commands.count_not_passed_tests()) + CEND + ' '*10)
    print("Num of configurations: " + str(at_commands.get_count()) + ' '*10)
    print('\033[10A', '\x1b[2K')

