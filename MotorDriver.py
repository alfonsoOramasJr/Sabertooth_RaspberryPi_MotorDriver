import serial

class MotorDriver:
    def __init__(self, port="/dev/ttyS0", baudrate=9600):
        self.serial_object = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        self.motor_ranges = {
            1:[0, 127],
            2:[128, 256]
        }

    ## Closes the serial port when a object from this class is deleted.
    def __del__(self):
        if self.serial_object and self.serial_object.isOpen():
            self.serial_object.close()
    
    def map_value(self, input_value, input_minimum, input_maximum, output_minimum, output_maximum):
        return output_minimum + (input_value - input_minimum) * (output_maximum - output_minimum) / (input_maximum - input_minimum)
    
