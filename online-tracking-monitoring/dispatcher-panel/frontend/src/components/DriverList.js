import React, { useEffect, useState } from 'react';
import { getDrivers } from '../api/dispatcherApi';

const DriverList = () => {
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    const fetchDrivers = async () => {
      const data = await getDrivers();
      setDrivers(data);
    };
    fetchDrivers();
  }, []);

  return (
    <div>
      <h2>Drivers</h2>
      <ul>
        {drivers.map((driver) => (
          <li key={driver.id}>{driver.name} - {driver.license_number}</li>
        ))}
      </ul>
    </div>
  );
};

export default DriverList;
