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
```