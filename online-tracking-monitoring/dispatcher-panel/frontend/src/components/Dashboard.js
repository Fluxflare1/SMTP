import React, { useState, useEffect } from 'react';
import VehicleCard from '../components/VehicleCard';
import { getVehicles } from '../services/api';

const Dashboard = () => {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        async function fetchData() {
            const response = await getVehicles();
            setVehicles(response);
        }
        fetchData();
    }, []);

    return (
        <div>
            <h2>Fleet Overview</h2>
            <div className="vehicle-list">
                {vehicles.map(vehicle => (
                    <VehicleCard key={vehicle.id} vehicle={vehicle} />
                ))}
            </div>
        </div>
    );
};

export default Dashboard;
