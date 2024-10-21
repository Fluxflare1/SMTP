import axios from 'axios';

const API_URL = 'http://localhost:8000/api'; // Update this based on your backend URL

export const getVehicles = async () => {
  const response = await axios.get(`${API_URL}/vehicles/`);
  return response.data;
};

export const getDrivers = async () => {
  const response = await axios.get(`${API_URL}/drivers/`);
  return response.data;
};

export const getTrips = async () => {
  const response = await axios.get(`${API_URL}/trips/`);
  return response.data;
};

export const createTrip = async (tripData) => {
  const response = await axios.post(`${API_URL}/trips/`, tripData);
  return response.data;
};
