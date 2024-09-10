import random

def generate_sensor_data(num_samples=2):
    data = {
        'accelerometer': [],
        'gyroscope': []
    }
    for _ in range(num_samples):
        acc_sample = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))
        gyro_sample = (random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-5, 5))
        data['accelerometer'].append(acc_sample)
        data['gyroscope'].append(gyro_sample)
    return data

# Simulate collecting 100 samples of sensor data
sensor_data = generate_sensor_data()
print(sensor_data)

import numpy as np

def extract_features(data):
    acc_data = np.array(data['accelerometer'])
    gyro_data = np.array(data['gyroscope'])

    features = {
        'acc_mean_x': np.mean(acc_data[:, 0]),
        'acc_mean_y': np.mean(acc_data[:, 1]),
        'acc_mean_z': np.mean(acc_data[:, 2]),
        'acc_std_x': np.std(acc_data[:, 0]),
        'acc_std_y': np.std(acc_data[:, 1]),
        'acc_std_z': np.std(acc_data[:, 2]),
        'gyro_mean_x': np.mean(gyro_data[:, 0]),
        'gyro_mean_y': np.mean(gyro_data[:, 1]),
        'gyro_mean_z': np.mean(gyro_data[:, 2]),
        'gyro_std_x': np.std(gyro_data[:, 0]),
        'gyro_std_y': np.std(gyro_data[:, 1]),
        'gyro_std_z': np.std(gyro_data[:, 2])
    }
    return features

# Extract features from the simulated data
features = extract_features(sensor_data)
print("Extracted Features:\n", features)

def estimate_road_condition(features):
    if features['acc_std_x'] > 5 or features['acc_std_y'] > 5 or features['acc_std_z'] > 5:
        return "Rough Road"
    elif features['gyro_std_x'] > 0.5 or features['gyro_std_y'] > 0.5 or features['gyro_std_z'] > 0.5:
        return "Curvy Road"
    else:
        return "Smooth Road"

# Estimate road condition based on extracted features
road_condition = estimate_road_condition(features)
print()
print("Estimated Road Condition:", road_condition)

