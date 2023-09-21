from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

# This script makes the end-effector perform pick, pour, and place tasks
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py'

def main():
    bot = InterbotixManipulatorXS("doris_arm", "arm", "gripper")
    bot.gripper.open()
    bot.gripper.close()
    bot.gripper.open()

if __name__=='__main__':
    main()
