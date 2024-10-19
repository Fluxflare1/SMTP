from sklearn.neighbors import KNeighborsRegressor

# Sample trip data (features: distance, traffic, weather)
X = trip_data[['distance', 'traffic', 'weather']]
y = trip_data['route_time']

# Train the model
model = KNeighborsRegressor()
model.fit(X, y)

# Predict optimal route time
def predict_optimal_route(trip_data):
    predicted_time = model.predict([trip_data])
    return predicted_time
