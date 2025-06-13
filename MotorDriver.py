import serial

class MotorDriver:
    def __init__(self, port="/dev/serial0", baudrate=9600):
        self.serial_object = serial.Serial(
            port=port,
            baudrate=baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

        self.motor_ranges = {
            1:[1, 127],
            2:[128, 255]
        }

    ## Closes the serial port when a object from this class is deleted.
    def close(self):
        if self.serial_object and self.serial_object.isOpen():
            self.serial_object.close()
    
    def map_value(self, input_value, input_minimum, input_maximum, output_minimum, output_maximum):
        return output_minimum + (input_value - input_minimum) * (output_maximum - output_minimum) / (input_maximum - input_minimum)
    
    def get_motor_ranges(self, motor_id):
        try:
            motor_range_minimum, motor_range_maximum = self.motor_ranges[motor_id]
            return motor_range_minimum, motor_range_maximum
        except KeyError:
            raise ValueError(f"Invalid motor_id: {motor_id}")

    def move_motor(self, motor_id, speed_in_percentages):
        motor_range_minimum, motor_range_maximum = self.get_motor_ranges(motor_id)
        motor_throttle = self.map_value(
            speed_in_percentages,
            -100, 100,
            motor_range_minimum, motor_range_maximum
        )
        byte_value = int(round(motor_throttle))
        self.serial_object.write(byte_value.to_bytes(1, "little"))