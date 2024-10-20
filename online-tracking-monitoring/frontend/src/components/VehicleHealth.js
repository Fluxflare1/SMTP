import React, { useEffect, useState } from 'react';

const VehicleHealth = ({ vehicle_id }) => {
    const [healthData, setHealthData] = useState({});

    useEffect(() => {
        fetch(`/api/vehicle/${vehicle_id}/health`)
            .then(response => response.json())
            .then(data => setHealthData(data));
    }, [vehicle_id]);

    return (
        <div>
            <h3>Vehicle {vehicle_id} Health Status</h3>
            <p>Engine Status: {healthData.engine_status}</p>
            <p>Temperature: {healthData.temperature}°C</p>
            <p>Maintenance Due: {healthData.maintenance_due ? 'Yes' : 'No'}</p>
        </div>
    );
};

export default VehicleHealth;
