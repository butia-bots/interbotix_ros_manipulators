from interbotix_xs_modules.arm import InterbotixManipulatorXS
# This script makes the end-effector go to a specific pose by defining the pose components
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python ee_pose_components.py'

def main():
    bot = InterbotixManipulatorXS("doris_arm", "arm", "gripper", moving_time=2, accel_time=0.3)
    bot.arm.set_ee_pose_components(x=0.3, z=0.3)

if __name__=='__main__':
    main()
