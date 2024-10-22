import React, { useState } from 'react';
import axios from 'axios';

const TripSchedule = () => {
    const [tripData, setTripData] = useState({
        vehicle: '',
        driver_name: '',
        destination: '',
        start_time: ''
    });

    const handleChange = (e) => {
        setTripData({ ...tripData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/schedule-trip/', tripData)
            .then(res => console.log(res.data))
            .catch(err => console.error(err));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="vehicle" placeholder="Vehicle" onChange={handleChange} />
            <input type="text" name="driver_name" placeholder="Driver Name" onChange={handleChange} />
            <input type="text" name="destination" placeholder="Destination" onChange={handleChange} />
            <input type="datetime-local" name="start_time" onChange={handleChange} />
            <button type="submit">Schedule Trip</button>
        </form>
    );
};

export default TripSchedule;
