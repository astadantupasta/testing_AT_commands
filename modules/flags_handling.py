import argparse

def get_flags():
    """Parses the command line arguments.
    :return: a list of flags
    """
    flagsParser = argparse.ArgumentParser()
    required_flags_group = flagsParser.add_argument_group('required named arguments')
    required_flags_group.add_argument("-n", "--name", help="name of the device", required=True)

    return flagsParser.parse_args()