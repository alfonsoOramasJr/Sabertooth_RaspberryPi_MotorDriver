# Sabertooth Dual 60A 6V-30V Regenerative Motor Driver
_Python software for the Sabertooth Motor Driver._

# Enabling Hardware Serial Port
Make sure to enable the hardware serial port through the interface options.

On a new terminal enter,
```
sudo raspi-config
```

And in the configuration menu, navigate to ```Interface Options```.

Click on ```Serial Port``` or what most closely resembles that option.

* When asked ```Login shell over serial?``` Select <strong>No</strong>.

* When asked ```Enable hardware serial port?``` Select <strong>Yes</strong>.

Reboot the device.

# Verifying that UART is Enabled

On a new terminal enter,
```
sudo nano /boot/config.txt
```

And make sure that ```enable_uart=1``` exists, it can typically be found near the bottom of the file.

# Using the MotorDriver Class
```python
from MotorDriver import MotorDriver
motor_driver = MotorDriver()
motor_driver.move_motor(1, 10) ## Moves the first motor by 10% of its maximum RPM.
motor_driver.move_motor(2, -20) ## Moves the second motor by 20% of its maximum RPM in the inverse direction.

motor_driver.move_motor(1, 0) ## Stops the first motor.
motor_driver.stop_all_motors() ## Stops all motors simultaneously by disabling output drive to the motors.
```

# Sabertooth Simplified Serial Mode Information
## Standard Simplified Serial Mode
For selecting the standard simplfied mode, mimic the following dip switch configuration, note that the baud rate is configured separately.
![alt text](<README_IMAGES/Standard Simplified Serial Mode.png>)

## Baud Rate is set by the Dip Switches
![alt text](<README_IMAGES/Baud Rate.png>)
For using the python software "out of the box," choose the ```9600 Baud Rate``` configuration.

If communication is not reliable, it is recommended to decrease the baud rate.

## Connecting the Transmit Line
From the host, connect the transmit line to S1. The host's receive line is not connected to the Sabertooth in Standard Simplified Serial Mode.

Note that when using a raspberry pi, you need to utilize a level shifter to send commands to the Sabertooh Driver. Something like this,

![alt text](<README_IMAGES/Logic Level Shifter.png>)

_Remember to not use the receive line in Simplified Serial Mode._

![alt text](<README_IMAGES/Level Shifter Connections.png>)
