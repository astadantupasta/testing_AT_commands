class AtCommands:
    def __init__(self, dictionary):
        """Initiation of AtCommands object from a dictionary.
        
        :dictionary: dictionary with at commands:
        command, expected_result, meaning
        """

        for key in dictionary:
            setattr(self, key, dictionary[key])

        self.received_result = ""
        self.test_is_passed = False

    def get_command(self):
        return self.command
    
    def get_expected_result(self):
        return self.expected_result
    
    def get_meaning(self):
        return self.meaning
    
    def get_received_result(self):
        return self.received_result
    
    def get_test_is_passed(self):
        return self.test_is_passed
    
    def set_test_is_passed(self):
        self.test_is_passed = (
            self.expected_result == self.received_result
        )