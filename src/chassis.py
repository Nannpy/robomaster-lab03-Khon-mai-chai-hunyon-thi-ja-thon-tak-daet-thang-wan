import time

class ChassisController:
    def __init__(self, ep_chassis, config):
        self.chassis = ep_chassis
        self.tile_size = config['tile_size_meter']
        self.speed = config['move_speed_mps']
        self.stop_time = config['stop_duration_sec']

    def move_one_tile_forward(self):
        #  Command the robot to move straight forward by a distance of one tile.
        print(f"[ACTION] Move forward {self.tile_size} เมตร")
        self.chassis.move(x=self.tile_size, y=0, z=0, xy_speed=self.speed).wait_for_completed()
        self._execution_stop()

    def turn_right_90_degree(self): 
        # Turn 90 degrees to the right, in a clockwise direction.
        print("[ACTION] Turn 90 degrees to the right")
        self.chassis.move(x=0, y=0, z=-90).wait_for_completed() 
        self._execution_stop()

    def _execution_stop(self):
        # Function to pause the system for a specified duration.
        print(f"[WAIT] Remain stationary for {self.stop_time} second")
        time.sleep(self.stop_time)