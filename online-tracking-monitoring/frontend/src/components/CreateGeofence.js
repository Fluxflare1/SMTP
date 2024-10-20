import React, { useState } from 'react';

const CreateGeofence = () => {
    const [name, setName] = useState('');
    const [latitude, setLatitude] = useState('');
    const [longitude, setLongitude] = useState('');
    const [radius, setRadius] = useState('');
    const [alertOnEnter, setAlertOnEnter] = useState(false);
    const [alertOnExit, setAlertOnExit] = useState(false);

    const handleSubmit = () => {
        fetch('/api/geofence/create', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                latitude,
                longitude,
                radius,
                alert_on_enter: alertOnEnter,
                alert_on_exit: alertOnExit,
            }),
        })
        .then(response => response.json())
        .then(data => alert(data.status));
    };

    return (
        <div>
            <h3>Create a Geofence</h3>
            <input type="text" placeholder="Name" value={name} onChange={e => setName(e.target.value)} />
            <input type="number" placeholder="Latitude" value={latitude} onChange={e => setLatitude(e.target.value)} />
            <input type="number" placeholder="Longitude" value={longitude} onChange={e => setLongitude(e.target.value)} />
            <input type="number" placeholder="Radius (meters)" value={radius} onChange={e => setRadius(e.target.value)} />
            <label>
                <input type="checkbox" checked={alertOnEnter} onChange={e => setAlertOnEnter(e.target.checked)} />
                Alert on Enter
            </label>
            <label>
                <input type="checkbox" checked={alertOnExit} onChange={e => setAlertOnExit(e.target.checked)} />
                Alert on Exit
            </label>
            <button onClick={handleSubmit}>Create Geofence</button>
        </div>
    );
};

export default CreateGeofence;
