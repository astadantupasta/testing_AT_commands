from modules.ICommunication import ICommunication
import paramiko
import time

class SshConnection(ICommunication):
    def __init__(self, hostname, username, password):
        """Initiate SSH connection.
        In case of connection error, code is stopped for waiting_seconds
        seconds repetition_times times.

        :hostname: ip address of the device
        :username: username for the ssh connection
        :password: password for the ssh connection
        :waiting_seconds: number of seconds that the code has to be stopped
        for until the next attempt to execute the command
        :repetition_times: number of repetitions until the code is exited
        """
        self.sshClient = paramiko.SSHClient()
        self.hostname = hostname
        self.username = username
        self.password = password

        self.__initiate()        

    def __initiate(self, waiting_seconds=5, repetition_times=10):
        """Connect to the device using SSH protocol.
        In case of connection error, code is stopped for waiting_seconds
        seconds repetition_times times.

        :hostname: ip address of the device
        :username: username for the ssh connection
        :password: password for the ssh connection
        :waiting_seconds: number of seconds that the code has to be stopped
        for until the next attempt to execute the command
        :repetition_times: number of repetitions until the code is exited
        """

        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for i in range(repetition_times):
            try:
                self.sshClient.connect(hostname=self.hostname, username=self.username, password=self.password)
                break
            except ConnectionError as e:
                print("Ssh connection error." + str(e))
                print("Make sure you indicated the correct device name and arguments.")
                print("reconnecting...")
                time.sleep(waiting_seconds)
            except Exception as e:
                print("Ssh connection error occured: " + str(e))
                print("Make sure you indicated the correct device name and arguments.")
                print("reconnecting...")
                time.sleep(waiting_seconds)

    def send_command(self, command, repetition_times=10):
        """Executes command on the device. In case of connection error, 
        code is stopped for waiting_seconds seconds repetition_times times.

        :command: command to execute
        :waiting_seconds: number of seconds that the code has to be stopped
        for until the next attempt to execute the command
        :repetition_times: number of repetitions until the code is exited
        :return: result of the command
        """
        response = self.send_command_when_expect(command, "OK", repetition_times)
        return response
    
    def send_command_when_expect(self, command, expected_response, repetition_times=5):
        """Sends command to the device until receives expected_response
        or repetition_times times.

        :command: command to send
        :expected_response: result that is expected as a response
        :repetition_times: number of times the command should be send
        if the response is not equal to the expected_response
        :return: the last line of the response (only "OK", "ERROR", "NO CARRIER")
        """
        response = ""
        count = 0
        while(response != expected_response):
            try:
                ssh_stdin, response, ssh_stderr = self.sshClient.exec_command("gsmctl -A " + command)
                ssh_stdin.close()
                break
            except:
                print("Executing ssh command failed. Command: " + command)
                print("reexecuting...")
                self.__initiate(self.hostname, self.username, self.password)
            count += 1

            if (count > repetition_times):
                return response
        return response.read().decode('ascii').strip()

    def open_port(self, repetition_times=20, waiting_seconds=5):
        pass

    def close_port(self):
        if self.sshClient.get_transport() is not None:
            self.sshClient.close()

    def check_connected_router_name(self, router_name):
        """Checks if products's name is as indicated in variable 'router_name'.
        :router_name: name of the router
        """
        ssh_stdout = self.send_command("cat /etc/config/system | grep routername | awk '{print $NF}' | sed \"s/'//g\"")
        if ssh_stdout != router_name:
            raise Exception("Connected product is not as indicated in variable 'router_name'")

    def check_modem(self):
        """Checks if product has a modem."""
        ssh_stdout = self.send_command("gsmctl -a")
        if ssh_stdout == "":
            raise Exception("The connected product does not have a modem.")

    def get_device_hostname(self):
        """Finds device hostname."""
        return self.send_command("cat /proc/sys/kernel/hostname")