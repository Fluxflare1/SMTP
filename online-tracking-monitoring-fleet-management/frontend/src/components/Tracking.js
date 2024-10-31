import React, { useEffect, useState } from 'react';
import { getTripStatus, getVehicleLocation } from '../services/api';

const Tracking = ({ vehicleId, tripId }) => {
    const [status, setStatus] = useState('');
    const [location, setLocation] = useState({ lat: 0, lng: 0 });

    useEffect(() => {
        const fetchStatus = async () => {
            const res = await getTripStatus(tripId);
            setStatus(res.data.status);
        };
        const fetchLocation = async () => {
            const res = await getVehicleLocation(vehicleId);
            setLocation(res.data.location);
        };

        fetchStatus();
        fetchLocation();
    }, [tripId, vehicleId]);

    return (
        <div>
            <h3>Trip Status: {status}</h3>
            <h3>Vehicle Location: {`Lat: ${location.lat}, Lng: ${location.lng}`}</h3>
        </div>
    );
};

export default Tracking;
