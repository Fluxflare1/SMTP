import React, { useState, useEffect } from 'react';
import apiClient from '../api/apiClient';

const NotificationPreferences = () => {
  const [preferences, setPreferences] = useState({
    geofenceAlerts: false,
    tripUpdates: false,
    maintenanceReminders: false,
  });

  useEffect(() => {
    // Fetch current preferences
    apiClient.get('/user/preferences/notifications')
      .then(response => setPreferences(response.data))
      .catch(error => console.error("Error loading preferences", error));
  }, []);

  const handleToggle = (type) => {
    setPreferences(prev => ({
      ...prev,
      [type]: !prev[type]
    }));
  };

  const savePreferences = () => {
    apiClient.post('/user/preferences/notifications', preferences)
      .then(() => alert("Preferences saved"))
      .catch(error => console.error("Error saving preferences", error));
  };

  return (
    <div className="notification-preferences">
      <h2>Notification Preferences</h2>
      <label>
        <input
          type="checkbox"
          checked={preferences.geofenceAlerts}
          onChange={() => handleToggle('geofenceAlerts')}
        />
        Geofence Alerts
      </label>
      <label>
        <input
          type="checkbox"
          checked={preferences.tripUpdates}
          onChange={() => handleToggle('tripUpdates')}
        />
        Trip Updates
      </label>
      <label>
        <input
          type="checkbox"
          checked={preferences.maintenanceReminders}
          onChange={() => handleToggle('maintenanceReminders')}
        />
        Maintenance Reminders
      </label>
      <button onClick={savePreferences}>Save</button>
    </div>
  );
};

export default NotificationPreferences;
