// frontend/src/components/RealTimeVehicleStatus.js

import React, { useEffect, useState } from 'react';
import { getRealTimeVehicleStatus } from '../services/vehicleService';

const RealTimeVehicleStatus = () => {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const data = await getRealTimeVehicleStatus();
                setVehicles(data);
            } catch (error) {
                console.error("Error loading vehicle status:", error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h2>Real-Time Vehicle Status</h2>
            <ul>
                {vehicles.map((vehicle) => (
                    <li key={vehicle.id}>
                        {vehicle.vehicle_name} - {vehicle.current_location || "Unknown Location"}
                        ({vehicle.availability_status})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RealTimeVehicleStatus;
