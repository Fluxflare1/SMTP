import React, { useEffect, useState } from 'react';

const IdleTime = ({ vehicle_id }) => {
    const [idleTime, setIdleTime] = useState(0);

    useEffect(() => {
        fetch(`/api/vehicle/${vehicle_id}/idle_time`)
            .then(response => response.json())
            .then(data => setIdleTime(data.idle_time));
    }, [vehicle_id]);

    return (
        <div>
            <h3>Vehicle {vehicle_id} Idle Time</h3>
            <p>{idleTime} seconds</p>
        </div>
    );
};

export default IdleTime;
