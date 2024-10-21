import React, { useEffect, useState } from 'react';
import { getTrips } from '../api/dispatcherApi';

const TripList = () => {
  const [trips, setTrips] = useState([]);

  useEffect(() => {
    const fetchTrips = async () => {
      const data = await getTrips();
      setTrips(data);
    };
    fetchTrips();
  }, []);

  return (
    <div>
      <h2>Trips</h2>
      <ul>
        {trips.map((trip) => (
          <li key={trip.id}>
            {trip.driver.name} is driving {trip.vehicle.number_plate} to {trip.destination}.
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TripList;
