// frontend/src/services/vehicleService.js

import axios from 'axios';

export const getRealTimeVehicleStatus = async () => {
    try {
        const response = await axios.get('/api/fleet_management/real-time-status/');
        return response.data;
    } catch (error) {
        console.error("Error fetching real-time vehicle status:", error);
        throw error;
    }
};
