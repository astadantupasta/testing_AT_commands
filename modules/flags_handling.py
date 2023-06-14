import argparse

def get_flags():
    """Parses the command line arguments.
    :return: a list of flags
    """
    flagsParser = argparse.ArgumentParser()
    required_flags_group = flagsParser.add_argument_group('required named arguments')
    required_flags_group.add_argument("-n", "--name", help="name of the device", required=True)
    required_flags_group.add_argument("-p", "--port", help="port", required=True)
    required_flags_group.add_argument("-pp", "--possibleport", help="another possible changed port after connection interuption", required=True)

    return flagsParser.parse_args()