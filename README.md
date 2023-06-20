# Testing AT commands
## Short description of the task
The purpose of this test automation is to test AT commands in the modem of the given product.
The test executes AT commands, compares received results with the expected ones and prints test statistics.

## Python library dependencies

One needs to install `argparse`, `python-abc`, `paramiko`, `prettytable`, `psutil` packages.
Installation can be done using
```
pip3 install *package_name*
```
command.

Versions used:
python-abc 0.2.0
paramiko 2.9.3
prettytable 3.7.0
psutil 5.9.5

## Configuration file
All information about the tested device and AT commands is stored in a JSON configuration file `at_commands.json`.

First of all, all the configurations are categorised according to the name of the device (e.g., `RUTX11`, `TRM240`, and etc.). Every device has its own `module`, `class`, and `at_commands`. The first two configurations (*module* and *class*) indicate the protocol that has to be used for communication. It can be either serial communication or the SSH protocol. For routers, the SSH protocol is used. In this case, *module* has to be set to `ssh_connection` and *class* to `SshConnection`. Modems use serial communication: *module* has to be set to `serial_communication` and *class* to `SerialCommunication`.

Every device has a different set of `at_commands`. Meanings of their values:
1. `command` indicates the AT command that has to be sent in order to receive a response.
2. `expected_response` indicated the value that is expected as a response.
3. `meaning` describes the meaning of the response (what does the received value represent).
Only test AT commands are used (the ones that return *OK*, *ERROR*, *NO CARRIES*, and etc. responses).

Example of the configuration file:
![at_commands](https://github.com/astadantupasta/testing_AT_commands/assets/79766133/61786cbd-509d-437f-9304-b4085a512a95)

## Build
1. Extract the zip file of this project, open it in Visual Studio Code.
2. Make sure that the configurations for connection are written correctly in the configuration file `at_commands.json`: locate the name of the router you are about to test, change *module*, *class* to the correct ones (either *ssh_connection* and *SshConnection*, or *serial_communication* and *SerialCommunication*).
3. Execute the proper command. Help for command can be seen when executing `python3 main.py -h`.
When SSH protocol is used, use command:
`python3 main.py -n NAME -p PORT -pp POSSIBLEPORT [-b BAUDRATE]`, where *name* is the name of the device (e.g., `RYTX11`, `TRM240`), *port* is a port used for connection and *possible_port* is a port that may be true after connection disruption.

When serial communication is used, use command:
`python3 main.py -n NAME -i IP -u USERNAME -pw PASSWORD`, where *name* is the name of the device, *ip* represents the hostname, *username* and *password* represent login information.
