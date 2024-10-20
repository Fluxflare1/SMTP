import React, { useEffect, useState } from 'react';

const FuelConsumption = ({ vehicle_id }) => {
    const [fuelData, setFuelData] = useState({});

    useEffect(() => {
        fetch(`/api/vehicle/${vehicle_id}/fuel_consumption`)
            .then(response => response.json())
            .then(data => setFuelData(data));
    }, [vehicle_id]);

    return (
        <div>
            <h3>Vehicle {vehicle_id} Fuel Consumption</h3>
            <p>Current Fuel Level: {fuelData.current_fuel_level} liters</p>
            <p>Average Fuel Consumption: {fuelData.average_fuel_consumption} liters/km</p>
        </div>
    );
};

export default FuelConsumption;
