# RoboMaster EP - Lab 03: Sensor Logging and Data Analysis

This project is part of the RoboMaster Laboratory course. It focuses on controlling the robot's movement based on specified distance parameters while logging real-time sensor data (Position, IMU, and Attitude). The logged data is subsequently processed and visualized to analyze the robot's physical behaviors.

## 📌 Team Members
* Mr. Thanarach Thepthun 6810110141
* Mr. Nannam Chaichanyut 6810110179
* Mr. Winyoo Singhsathon 6810110324
* Mr. Siwakorn Saengkaew 6810110717

## 🎬 Video Demonstration
* https://youtu.be/pj8nJ7THZvQ?si=xdTwhRsYq7rNZUPS

## 📝 Experimental Conclusion

In this experiment, the RoboMaster EP robot was programmed to move forward by 58 cm and execute a 90-degree right turn, repeating this sequence for a total of 4 cycles. The robot was configured to pause and remain stationary for 1.0 second at every destination point. Sensor telemetry was logged via the Data Logging API at a sampling frequency of 5 Hz. Based on the generated visualization charts, the physical behaviors can be analyzed as follows:

### 1. Position Verification (Robot Position over Time)
* The trajectory curves for the `X` axis (Forward) and `Y` axis (Left/Right) exhibit clear, alternating stepped transitions corresponding to each positional movement phase.
* Distinct flat intervals where the slope equals zero ($\text{Slope} = 0$) are visible parallel to the time axis immediately following each motion phase. This provides empirical evidence confirming that **the robot remained completely stationary for 1.0 second at every designated point** as specified by the requirements.

### 2. Transient Shock and Acceleration Analysis (IMU Linear Acceleration)
* The linear acceleration data from the IMU for both `Acceleration X` and `Acceleration Y` axes shows prominent sharp peaks and drops (Spikes). These occur exclusively during **"initial acceleration phases (takeoff)"** and **"sudden deceleration phases (braking)"**.
* During the 1-second stationary intervals, the acceleration curves stabilize back to near `0 m/s²`, with minimal deviations caused only by residual sensor noise.

### 3. Rotational Attitude Verification (Yaw Angle)
* The `Yaw (Orientation)` curve shows a well-defined staircase pattern, decreasing by approximately 90 degrees (angular orientation shift along the Z-axis) per step for a total of **4 distinct steps**.
* This consistent 90-degree descending staircase profile verifies that the mecanum-wheeled chassis successfully executed precise **clockwise (right) turns** in strict accordance with the control loop logic.

**Overall Summary:** The chassis motion controller and the data logging module operated in perfect synchronization. The raw telemetry captured within the `sensor_logs.csv` file proves to be highly accurate and fully complies with the kinematic theories governing omnidirectional mecanum-wheeled robot locomotion.