import time
from mpu6050 import mpu6050

mpu6050 = mpu6050.mpu6050(0x68)

def read_sensor_data():
    acc_data = mpu6050.get_accel_data()
    gyro_data = mpu6050.get_gyro_data()
    t = mpu6050.get_temp()

    return acc_data, gyro_data, t

while True:
    acc_data, gyro_data, t = read_sensor_data()
    print(f"Acceleration: {acc_data}")
    print(f"Gyro: {gyro_data}")
    print(f"Temperature: {t}")
    time.sleep(0.1)
