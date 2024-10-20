import React from 'react';

const ImmobilizeVehicle = ({ vehicle_id }) => {
    const handleClick = () => {
        fetch(`/api/vehicle/${vehicle_id}/immobilize`, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <button onClick={handleClick}>
            Immobilize Vehicle
        </button>
    );
};

export default ImmobilizeVehicle;
