import React, { useState } from 'react';
import { scheduleTrip } from '../services/api';

const TripScheduler = () => {
    const [tripData, setTripData] = useState({ vehicle: '', driver: '', origin: '', destination: '', time: '' });

    const handleChange = (e) => {
        setTripData({ ...tripData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await scheduleTrip(tripData);
            alert('Trip scheduled successfully');
        } catch (error) {
            alert('Failed to schedule trip');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            {/* Fields for vehicle, driver, origin, destination, and time */}
            <button type="submit">Schedule Trip</button>
        </form>
    );
};

export default TripScheduler;
