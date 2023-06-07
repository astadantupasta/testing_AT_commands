import json

def read_data_from_json(file_name, device_name):
    """Read data from json file.
    
    :file_name: name of the json file
    :return: dictionary read from the json file
    """
    try:
        with open(file_name, "r") as read_file:
            try:
                data = json.load(read_file)[device_name]
            except KeyError as e:
                print("'" + device_name + "': name of the device not found.")
                print("Please check and execute the command again.")
                exit()
        return data
    except FileNotFoundError:
        print("No such file: " + file_name)