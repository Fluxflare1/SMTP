import React, { useState, useEffect } from 'react';
import { getVehicles } from './api';

function App() {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        getVehicles().then((response) => {
            setVehicles(response.data);
        });
    }, []);

    return (
        <div className="App">
            <h1>Vehicle Tracking</h1>
            <table>
                <thead>
                    <tr>
                        <th>Vehicle ID</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                        <th>Speed</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {vehicles.map(vehicle => (
                        <tr key={vehicle.vehicle_id}>
                            <td>{vehicle.vehicle_id}</td>
                            <td>{vehicle.current_latitude}</td>
                            <td>{vehicle.current_longitude}</td>
                            <td>{vehicle.current_speed}</td>
                            <td>{vehicle.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default App;
