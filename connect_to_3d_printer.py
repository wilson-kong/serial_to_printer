import serial.tools.list_ports
import time

# Constants
PORT = 'COM5'                   # COM port the printer is connected to. for Mac: '/dev/ttyUSB0'
BAUD_RATE = 115200              # Baud rate, should be fixed
FILE_NAME = 'movement.gcode'    # input file for movement.

# connection to printer
serial_port = serial.Serial(PORT, BAUD_RATE)

print(f'{serial_port} is open.')

time.sleep(2)

def parse_gcode(gcode_raw: str):
    """
    Pasrses gcode to something readable by the machine.
    Parameters:
        gcode_raw (str): line of gcode to be parsed
    Returns:
        (str): parsed gcode with a new line charater added.
    """
    actual, _, _ = gcode_raw.partition(';')
    actual = actual.strip()
    actual += '\n'
    return actual

# read and process gcode file
with open(FILE_NAME, 'r') as file:
    gcode = [parse_gcode(i).encode('ascii') for i in file]

# write to 3D printer
for code in gcode:
    serial_port.write(code)

# shut down
time.sleep(2)
serial_port.close()
