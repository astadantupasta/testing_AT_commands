import psutil
import os, signal

def kill_process(proc_name):
    """Kill process, indicates as a proc_name.
    :proc_name: name of the process to kill
    """
    for proc in psutil.process_iter():
        # Check if the process name matches
        if proc.name() == proc_name:
            try:
                os.system("sudo kill %s" % (proc.pid, ))
            except Exception as e:
                print("Error occured when killing the process: " + str(e))

def kill_modem_manager():
    kill_process("ModemManager")

def provide_permission(file_path, permission):
    """Provides permission for the indicated file.
    :file_path: path of the file
    :permission: permission which is to be granted
    """
    try:
        #os.chmod(file_path, permission)
        os.system("sudo chmod %s %s" % (permission, file_path))
    except Exception as e:
        print("Error occured when providing permission: " + str(e))

def provide_read_write_permission(file_path):
    """Provides read/write permission for the
    indicated file.
    :file_path: path of the file
    """
    provide_permission(file_path, 666)
