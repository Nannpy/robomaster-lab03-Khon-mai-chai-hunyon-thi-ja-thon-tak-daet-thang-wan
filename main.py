import robomaster
from robomaster import robot
from src.config_loader import load_settings
from src.logger import RobotDataLogger
from src.chassis import ChassisController

def main():
    config = load_settings()
    robot_cfg = config['robot']['connection']
    chassis_cfg = config['robot']['chassis']
    
    robomaster.config.LOCAL_IP_STR = robot_cfg['local_ip']
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type=robot_cfg['type'])
    
    logger = RobotDataLogger()
    logger.start_logging(ep_robot)
    
    controller = ChassisController(ep_robot.chassis, chassis_cfg)
    
    try:
        print("\n=== Start by moving forward 70 cm and turning right four times ===")
        
        for side in range(4):
            print(f"\n--- running lap number {side + 1} ---")
            
            # Move forward 70 cm and stop for 1 second
            controller.move_one_tile_forward()
            
            # Rotate 90 degrees to the right
            controller.turn_right_90_degree()
                
        print("\n=== Dona all mission ===")
        
    except KeyboardInterrupt:
        print("\n[WARNING] Interrupt by user")
    finally:
        logger.save_and_stop(ep_robot)
        ep_robot.close()

if __name__ == '__main__':
    main()