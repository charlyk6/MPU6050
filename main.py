import math
import time
from mpu6050 import mpu6050

sensor = mpu6050(0x68)


def accel_to_pitch_roll(acc):
    """Углы наклона в градусах из данных акселерометра (g по осям)."""
    ax, ay, az = acc["x"], acc["y"], acc["z"]
    roll = math.degrees(math.atan2(ay, az))
    pitch = math.degrees(math.atan2(-ax, math.sqrt(ay * ay + az * az)))
    return pitch, roll


def read_sensor_data():
    acc_data = sensor.get_accel_data()
    t = sensor.get_temp()
    return acc_data, t


while True:
    acc_data, t = read_sensor_data()
    pitch, roll = accel_to_pitch_roll(acc_data)
    print(f"Pitch: {pitch:7.2f}°  Roll: {roll:7.2f}°  |  T: {t}")
    time.sleep(0.1)
