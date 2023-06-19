import argparse

def get_flags():
    """Parses the command line arguments.
    :return: a list of flags
    """
    flagsParser = argparse.ArgumentParser(usage=msg())
    serial_flags_group = flagsParser.add_argument_group('required arguments for serial communication')
    ssh_flags_group = flagsParser.add_argument_group('required arguments for ssh connection')

    flagsParser.add_argument("-n", "--name", help="name of the device", required=True)

    serial_flags_group.add_argument("-p", "--port", help="port", required=False)
    serial_flags_group.add_argument("-pp", "--possibleport", help="another possible changed port after connection interuption")
    serial_flags_group.add_argument("-b", "--baudrate", help="baudrate of the port", required=False)

    ssh_flags_group.add_argument('-i', "--ip", help="hostname of the device")
    ssh_flags_group.add_argument('-u', '--username', help="username")
    ssh_flags_group.add_argument('-pw', '--password', help="password")

    return flagsParser.parse_args()

def get_communication_arguments(flags):
    """Returns arguments needed for different communication types.
    :return: device_name, first_arg, second_arg, third_arg
    """
    device_name = flags.name.upper()
    if flags.port: first_arg = flags.port
    if flags.possibleport: second_arg = flags.possibleport
    if flags.baudrate: third_arg = flags.baudrate
    else: third_arg = 9600
    if flags.ip: first_arg = flags.ip
    if flags.username: second_arg = flags.username
    if flags.password: third_arg = flags.password

    return device_name, first_arg, second_arg, third_arg
    

def msg(name=None):
    return '''Usage for SSH connection:
    main.py -n NAME -p PORT -pp POSSIBLEPORT [-b BAUDRATE]

    Usage for Serial communication:
    main.py -n NAME -i IP -u USERNAME -pw PASSWORD
    '''

def test_flags(flags):
    if flags.port and (not flags.possibleport):
        print("Usage for SSH connection:")
        print("main.py -n NAME -p PORT -pp POSSIBLEPORT [-b BAUDRATE]")
        exit()
    
    if flags.ip and ((not flags.username) or (not flags.password)):
        print("Usage for Serial communication:")
        print("main.py -n NAME -i IP -u USERNAME -pw PASSWORD")
        exit()

    if flags.name and ((not flags.ip) and (not flags.port)):
        print("Possible usages:")
        print("main.py -n NAME -p PORT -pp POSSIBLEPORT [-b BAUDRATE]")
        print("main.py -n NAME -i IP -u USERNAME -pw PASSWORD")
        exit()