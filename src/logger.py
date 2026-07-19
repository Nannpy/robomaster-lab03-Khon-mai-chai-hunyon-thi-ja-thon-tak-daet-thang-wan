import os
import time
import pandas as pd

class RobotDataLogger:
    def __init__(self):
        self.data_records = []
        self.start_time = None
        
        # Automatically create a folder structure for storing raw data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(current_dir, '..', 'data', 'raw', f"run_{time.strftime('%Y%m%d_%H%M%S')}")
        os.makedirs(self.output_dir, exist_ok=True)
        self.csv_path = os.path.join(self.output_dir, 'sensor_logs.csv')

    def start_logging(self, ep_robot):
        # Register to subscribe to sensor data via callback.
        self.start_time = time.time()
        
        # Subscribe to wheelbase coordinate sensor data, pose data and Inertial Measurement Unit (IMU) data
        ep_robot.chassis.sub_position(freq=5, callback=self._position_handler)
        ep_robot.chassis.sub_attitude(freq=5, callback=self._attitude_handler)
        ep_robot.chassis.sub_imu(freq=5, callback=self._imu_handler)
        
        self.current_state = {'x': 0.0, 'y': 0.0, 'z': 0.0, 'pitch': 0.0, 'roll': 0.0, 'yaw': 0.0, 'acc_x': 0.0, 'acc_y': 0.0, 'acc_z': 0.0}

    def _position_handler(self, pos_info):
        x, y, z = pos_info
        self.current_state.update({'x': x, 'y': y, 'z': z})
        self._record_row()

    def _attitude_handler(self, att_info):
        yaw, pitch, roll = att_info
        self.current_state.update({'yaw': yaw, 'pitch': pitch, 'roll': roll})

    def _imu_handler(self, imu_info):
        acc_x, acc_y, acc_z, _, _, _ = imu_info
        self.current_state.update({'acc_x': acc_x, 'acc_y': acc_y, 'acc_z': acc_z})

    def _record_row(self):
        # Compile the information and calculate the duration, then add it to the list
        if self.start_time is None:
            return
            
        timestamp = time.time() - self.start_time
        row = {'timestamp': timestamp}
        row.update(self.current_state)
        self.data_records.append(row)
        
        # Print the statistics to the console as specified in the problem
        print(f"[LOG] Time: {timestamp:.2f}s | Pos: (X:{row['x']:.2f}, Y:{row['y']:.2f}) | Yaw: {row['yaw']:.1f}°")

    def save_and_stop(self, ep_robot):
        # Cancel data reception and export all recorded data to a csv file
        ep_robot.chassis.unsub_position()
        ep_robot.chassis.unsub_attitude()
        ep_robot.chassis.unsub_imu()
        
        if self.data_records:
            df = pd.DataFrame(self.data_records)
            df.to_csv(self.csv_path, index=False)
            print(f"\n[SUCCESS] The sensor data file has been successfully saved to : {self.csv_path}")