import React, { useState, useEffect } from 'react';
import axios from 'axios';

function VehicleDistance({ vehicleId }) {
  const [totalDistance, setTotalDistance] = useState(0);

  useEffect(() => {
    const fetchDistance = () => {
      axios.get(`/api/update-vehicle-location/${vehicleId}/?latitude=10.123&longitude=12.456`)
        .then(response => {
          setTotalDistance(response.data.total_distance_traveled);
        })
        .catch(error => {
          console.log('Error fetching distance:', error);
        });
    };

    fetchDistance();
  }, [vehicleId]);

  return (
    <div>
      <h3>Vehicle ID: {vehicleId}</h3>
      <p>Total Distance Traveled: {totalDistance.toFixed(2)} km</p>
    </div>
  );
}

export default VehicleDistance;
