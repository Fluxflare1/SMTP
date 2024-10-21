
import React, { useState } from 'react';
import axios from 'axios';

const TripForm = () => {
  const [formData, setFormData] = useState({
    vehicle: '',
    start_location: '',
    destination: '',
    scheduled_time: ''
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/trip-schedule/', formData)
      .then(response => {
        alert('Trip scheduled successfully!');
      })
      .catch(error => {
        console.error('There was an error scheduling the trip!', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>Vehicle ID:</label>
      <input type="text" value={formData.vehicle} onChange={e => setFormData({...formData, vehicle: e.target.value})} />
      <label>Start Location:</label>
      <input type="text" value={formData.start_location} onChange={e => setFormData({...formData, start_location: e.target.value})} />
      <label>Destination:</label>
      <input type="text" value={formData.destination} onChange={e => setFormData({...formData, destination: e.target.value})} />
      <label>Scheduled Time:</label>
      <input type="datetime-local" value={formData.scheduled_time} onChange={e => setFormData({...formData, scheduled_time: e.target.value})} />
      <button type="submit">Schedule Trip</button>
    </form>
  );
};

export default TripForm;
