

from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Sample training data
data = pd.read_csv('vehicle_data.csv')

# Features: acceleration, speed, braking, cornering, phone usage
X = data[['acceleration', 'speed', 'braking', 'cornering', 'phone_usage']]
y = data['harsh_event']  # Target: 0 = No, 1 = Yes

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Predict behavior
def predict_behavior(vehicle_data):
    prediction = model.predict([vehicle_data])
    return prediction[0]

def predict_and_monitor_behavior(vehicle_data):
    behavior_prediction = predict_behavior(vehicle_data)
    if behavior_prediction == 1:
        trigger_geofence_alert(vehicle_data['vehicle_id'], "predicted harsh event", "detected")






from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Sample training data
data = pd.read_csv('vehicle_data.csv')

# Features: acceleration, speed, braking
X = data[['acceleration', 'speed', 'braking']]
y = data['harsh_event']  # Target: 0 = No, 1 = Yes

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Predict behavior
def predict_behavior(vehicle_data):
    prediction = model.predict([vehicle_data])
    return prediction[0]

def predict_and_monitor_behavior(vehicle_data):
    behavior_prediction = predict_behavior(vehicle_data)
    if behavior_prediction == 1:
        trigger_geofence_alert(vehicle_data['vehicle_id'], "predicted harsh event", "detected")
