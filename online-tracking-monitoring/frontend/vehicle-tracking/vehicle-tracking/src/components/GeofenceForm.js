import React, { useState } from 'react';
import axios from 'axios';

const GeofenceForm = () => {
    const [name, setName] = useState('');
    const [latitude, setLatitude] = useState('');
    const [longitude, setLongitude] = useState('');
    const [radius, setRadius] = useState('');

    const createGeofence = (e) => {
        e.preventDefault();

        const geofence = {
            name: name,
            center_latitude: parseFloat(latitude),
            center_longitude: parseFloat(longitude),
            radius_in_km: parseFloat(radius),
        };

        axios.post('http://localhost:8000/api/geofences/', geofence)
            .then(response => {
                console.log("Geofence created:", response.data);
                alert("Geofence created successfully!");
            })
            .catch(error => {
                console.error("There was an error creating the geofence!", error);
            });
    };

    return (
        <form onSubmit={createGeofence}>
            <h2>Create a Geofence</h2>
            <input type="text" placeholder="Geofence Name" value={name} onChange={e => setName(e.target.value)} required />
            <input type="text" placeholder="Latitude" value={latitude} onChange={e => setLatitude(e.target.value)} required />
            <input type="text" placeholder="Longitude" value={longitude} onChange={e => setLongitude(e.target.value)} required />
            <input type="text" placeholder="Radius (in km)" value={radius} onChange={e => setRadius(e.target.value)} required />
            <button type="submit">Create Geofence</button>
        </form>
    );
};

export default GeofenceForm;
