import subprocess

def get_sensor_data(sensor_id):
    command = f"adb shell dumpsys sensorservice | grep -A 50 {sensor_id} | grep -oE '\-?[0-9]+(\.[0-9]+)?, \-?[0-9]+(\.[0-9]+)?, \-?[0-9]+(\.[0-9]+)?' | grep -v '),' | sed 's/, $//'"
    output = subprocess.check_output(command, shell=True)
    sensor_data = parse_sensor_data(output)
    return sensor_data


def parse_sensor_data(output):
    lines = output.decode().split('\n')
    sensor_data = []
    for line in lines:
        values = line.strip().split(', ')
        if len(values) == 3:
            sensor_data.append([float(value) for value in values])
    return sensor_data

if __name__ == "__main__":
    sensor_id = "'icm4x6xx Accelerometer Non-wakeup'"
    data = get_sensor_data(sensor_id)
    if data:
        print("Sensor Data:")
        for sensor_data in data:
            print(sensor_data)
    else:
        print("Failed to retrieve sensor data.")

