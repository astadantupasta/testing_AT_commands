import serial
import time

class SerialCommunication:
    def __init__(self, port, baudrate=9600, timeout=.1):
        """Initiation of the object which establishes a serial communication.

        :port: device name, port used for serial communication
        :baudrate: baudrate such as 9600 ar 115200
        :timeout: read timeout value in seconds
        """
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)

    def __send_command(self, command):
        """Sends command to device.
        
        :command: command to send
        :return: a list of received responses after sending the command
        """
        self.ser.write(bytes(command+"\r\n", "ascii"))
        time.sleep(0.2)
        ret=[]
        while self.ser.in_waiting > 0:
            msg = self.ser.readline().strip()
            msg = msg.replace(b'\r', b'')
            msg = msg.replace(b'\r', b'')
            if msg != "":
                ret.append(bytes.decode(msg, 'ascii'))
        return ret
    
    def send_command_when_expect(self, command, expected_response, repetition_times=5):
        """Sends command to the device until receives expected_response
        or repetition_times times.

        :command: command to send
        :expected_response: result that is expected as a response
        :repetition_times: number of times the command should be send
        if the response is not equal to the expected_response
        :return: the last line of the response (only "OK", "ERROR", "NO CARRIER")
        """ 
        # Check if the port is open. If not, reopen
        self.open_port()

        response = ""
        count = 0
        while(response != expected_response):
            try:
                answer = self.__send_command(command)
                response = answer[-1]
            except IndexError as e:
                print("No response received: " + str(e))
                print(command)
                print(answer)
            count += 1
            if(count > repetition_times):
                return response    
        return response

    def send_command(self, command, repetition_times=5):
        """Sends command to the device until receives response
        or repetition_times times.

        :command: command to send
        :repetition_times: number of times the command should be send
        if the response is not equal to the expected_response
        :return: response
        """ 
        self.open_port()

        response_ok = ""
        count = 0
        while(response_ok != "OK"):
            response = self.__send_command(command)
            try:
                response_ok = response[-1]
            except IndexError as e:
                print("No response received: " + str(e))
            count += 1

            if(count > repetition_times):
                return response[1]
            
        return response[1]
    
    def open_port(self):
        """Opens the port, if it is not already open."""
        try:
            if self.ser.closed:
                self.ser.open()
        except Exception as e:
            print("Error while openning the port: " + str(e))

    def close_port(self):
        """Closes the port, if it is not already closed."""
        try:
            if self.ser.is_open:
                self.ser.close()
        except Exception as e:
            print("Error while closing the port: " + str(e))



