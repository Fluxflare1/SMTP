


import React, { useState } from 'react';
import axios from 'axios';

function VehicleControl({ vehicleId, isImmobilized }) {
  const [immobilized, setImmobilized] = useState(isImmobilized);

  const toggleImmobilization = () => {
    const endpoint = immobilized ? `/api/release-immobilization/${vehicleId}/` : `/api/immobilize/${vehicleId}/`;
    
    axios.post(endpoint)
      .then(response => {
        setImmobilized(!immobilized);
      })
      .catch(error => {
        console.log('Error immobilizing vehicle:', error);
      });
  };

  return (
    <div>
      <h3>Vehicle ID: {vehicleId}</h3>
      <p>Status: {immobilized ? 'Immobilized' : 'Active'}</p>
      <button onClick={toggleImmobilization}>
        {immobilized ? 'Release Immobilization' : 'Immobilize'}
      </button>
    </div>
  );
}

export default VehicleControl;
