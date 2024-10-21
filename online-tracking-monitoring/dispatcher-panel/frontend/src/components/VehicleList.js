

import React, { useEffect, useState } from 'react';
import { getVehicles } from '../api/dispatcherApi';

const VehicleList = () => {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    const fetchVehicles = async () => {
      const data = await getVehicles();
      setVehicles(data);
    };
    fetchVehicles();
  }, []);

  return (
    <div>
      <h2>Vehicles</h2>
      <ul>
        {vehicles.map((vehicle) => (
          <li key={vehicle.id}>{vehicle.number_plate} - {vehicle.status}</li>
        ))}
      </ul>
    </div>
  );
};

export default VehicleList;



import React, { useEffect, useState } from 'react';
import axios from 'axios';

const VehicleList = () => {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    axios.get('/api/vehicles/')
      .then(response => {
        setVehicles(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the vehicles!', error);
      });
  }, []);

  return (
    <div>
      <h2>Vehicle List</h2>
      <ul>
        {vehicles.map(vehicle => (
          <li key={vehicle.id}>{vehicle.name} - {vehicle.status}</li>
        ))}
      </ul>
    </div>
  );
}

export default VehicleList;
