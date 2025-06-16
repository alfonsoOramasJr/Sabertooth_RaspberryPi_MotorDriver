import time
from MotorDriver import MotorDriver

motor_driver = MotorDriver()

motor_driver.move_motor(1, 5)
motor_driver.move_motor(2, 5)
time.sleep(2)

motor_driver.move_motor(1, 0)
motor_driver.move_motor(2, 0)
motor_driver.stop_all_motors()
motor_driver.close()