import sys
import urx
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper

robot = urx.Robot("128.30.31.95")
grip = Robotiq_Two_Finger_Gripper(robot)

# grip.activate_gripper()

# grip.open_gripper()

# grip.close_gripper()

# robot.set_analog_out_to_pos()

# time.sleep(0.5)

# data = robot.secmon.get_all_data(wait=False)

# print("\n  !----- analog state open: ", data['MasterBoardData']['analogOutput0'], '\n')

# time.sleep(1)