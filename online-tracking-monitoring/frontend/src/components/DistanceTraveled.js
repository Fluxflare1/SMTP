import React, { useEffect, useState } from 'react';

const DistanceTraveled = ({ vehicle_id }) => {
    const [distance, setDistance] = useState(0);

    useEffect(() => {
        fetch(`/api/vehicle/${vehicle_id}/distance`)
            .then(response => response.json())
            .then(data => setDistance(data.total_distance));
    }, [vehicle_id]);

    return (
        <div>
            <h3>Vehicle {vehicle_id} Distance Traveled</h3>
            <p>{distance} km</p>
        </div>
    );
};

export default DistanceTraveled;
