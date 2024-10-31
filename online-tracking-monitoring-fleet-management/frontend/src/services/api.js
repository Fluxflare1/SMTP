import axios from 'axios';

const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Trip Scheduling
export const scheduleTrip = (tripData) => api.post('/trips/', tripData);

// Trip Tracking
export const getTripStatus = (tripId) => api.get(`/trips/${tripId}/status`);
export const getVehicleLocation = (vehicleId) => api.get(`/vehicles/${vehicleId}/location`);

// Notifications
export const getNotifications = (userId) => api.get(`/notifications/${userId}`);

export default api;
