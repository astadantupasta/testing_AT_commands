class AtCommand:
    def __init__(self, dictionary):
        """Initiation of AtCommands object from a dictionary.
        
        :dictionary: dictionary with at commands:
        command, expected_response, meaning
        """

        for key in dictionary:
            setattr(self, key, dictionary[key])

        self.received_response = ""
        self.test_is_passed = False

    def get_command(self):
        return self.command
    
    def get_expected_response(self):
        return self.expected_response
    
    def get_meaning(self):
        return self.meaning
    
    def get_received_response(self):
        return self.received_response
    
    def get_test_is_passed(self):
        return self.test_is_passed
    
    def get_all_values(self):
        """Returns a list of all values in orderL
        meaning, command, expected_response,
        received_response, test_is_passed.
        
        :return: a list of all variable values
        """
        return [self.get_meaning(), 
                self.get_command(),
                self.get_expected_response(),
                self.get_received_response(),
                self.get_test_is_passed()]
    
    def set_received_response(self, received_response):
        self.received_response = received_response
        self.set_test_is_passed()
    
    def set_test_is_passed(self):
        self.test_is_passed = (
            self.get_expected_response() == self.get_received_response()
        )
