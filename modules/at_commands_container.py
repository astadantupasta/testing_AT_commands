from modules.at_command import AtCommand

from modules import print_to_terminal

class AtCommandsContainer:
    def __init__(self, dictionaries):
        """Initiates an AtCommands container object
        from a list of dictionaries.
        
        :dictionaries: a list of dictionaries
        """

        self.at_commands = []
        self.module = dictionaries['module']
        self.myclass = dictionaries['class']
        for dictionary in dictionaries['at_commands']:
            self.at_commands.append(AtCommand(dictionary))

        self.modem_manufacturer = ""
        self.modem_model = ""
    
    def set_modem_manufacturer(self, serial):
        """Sends AT command and sets the received response.
        :serial: SerialCommunication object
        """
        self.modem_manufacturer = serial.send_command(command="AT+GMI")
    
    def set_modem_model(self, serial):
        """Sends AT command and sets the received response.
        :serial: SerialCommunication objetc
        """
        self.modem_model = serial.send_command(command="AT+GMM")

    def get_count(self):
        return len(self.at_commands)
    
    def get_modem_manufacturer(self):
        return self.modem_manufacturer
    
    def get_modem_model(self):
        return self.modem_model
    
    def get_module(self):
        return self.module
    
    def get_class(self):
        return self.myclass

    def set_at_commands_responses(self, serial):
        """Sends AT commands and sets the received 
        responses to AtCommand.received_response variable.
        
        :serial: SerialCommunication object
        """
        for at_command in self.at_commands:
            response = serial.send_command_when_expect(at_command.get_command(), at_command.get_expected_response())
            at_command.set_received_response(response)

            print_to_terminal.print_one_command(at_command)

    def check_if_tests_are_passed(self):
        """Checks if tests are passed (expected and received responses
        are similar) and sets a variable AtCommands.test_is_passed."""

        for at_command in self.at_commands:
            at_command.set_test_is_passed()

    def count_passed_tests(self):
        """Counts how many tests have been passed.
        :return: number of passed tests
        """
        counter = 0
        for at_command in self.at_commands:
            if at_command.get_test_is_passed():
                counter += 1
        return counter
    
    def count_not_passed_tests(self):
        """Counts how many tests have not been passed.
        :return: number of not passed tests
        """
        return self.get_count() - self.count_passed_tests()
    
    def get_list_of_attribute_names(self):
        """Returns a list of attribute names that are stored
        in each AtCommand object.
        
        :return: list of attribute names stored in each AtCommand object.
        """

        at_command = self.at_commands[0]
        attributes = [attr for attr in dir(at_command) if not callable(getattr(at_command, attr) and not attr.startswith("__"))] 
        return attributes
    
    def yield_at_commands(self):
        """Yields AtCommand object.
        :return: AtCommand object
        """
        for at_command in self.at_commands:
            yield at_command






