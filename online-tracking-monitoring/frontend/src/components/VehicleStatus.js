import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VehicleStatus({ vehicleId }) {
  const [idleDuration, setIdleDuration] = useState(0);

  useEffect(() => {
    const fetchIdleStatus = () => {
      axios.get(`/api/check-idle-time/${vehicleId}/`)
        .then(response => {
          setIdleDuration(response.data.idle_duration);
        })
        .catch(error => {
          console.log('Error fetching idle status:', error);
        });
    };

    fetchIdleStatus();
    const interval = setInterval(fetchIdleStatus, 60000);  // Check every minute
    return () => clearInterval(interval);
  }, [vehicleId]);

  return (
    <div>
      <h3>Vehicle ID: {vehicleId}</h3>
      <p>{idleDuration > 0 ? `Idle for ${idleDuration} minutes` : 'Active'}</p>
    </div>
  );
}

export default VehicleStatus;
