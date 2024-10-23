import React from 'react';

const VehicleCard = ({ vehicle }) => {
    return (
        <div className="vehicle-card">
            <h3>{vehicle.name}</h3>
            <p>License Plate: {vehicle.license_plate}</p>
            <p>Status: {vehicle.status}</p>
        </div>
    );
};

export default VehicleCard;
