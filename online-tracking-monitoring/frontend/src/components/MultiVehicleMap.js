import React, { useEffect, useState } from 'react';
import GoogleMapReact from 'google-map-react';

const VehicleMarker = ({ text }) => <div>{text}</div>;

const MultiVehicleMap = () => {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        // Fetch vehicles data from the backend
        fetch('/api/vehicles/location')
            .then(response => response.json())
            .then(data => setVehicles(data.vehicles));
    }, []);

    const center = {
        lat: vehicles.length ? vehicles[0].latitude : 0,
        lng: vehicles.length ? vehicles[0].longitude : 0
    };

    const zoom = 10;

    return (
        <div style={{ height: '100vh', width: '100%' }}>
            <GoogleMapReact
                bootstrapURLKeys={{ key: 'YOUR_GOOGLE_MAPS_API_KEY' }}
                defaultCenter={center}
                defaultZoom={zoom}
            >
                {vehicles.map(vehicle => (
                    <VehicleMarker
                        key={vehicle.vehicle_id}
                        lat={vehicle.latitude}
                        lng={vehicle.longitude}
                        text={vehicle.vehicle_id}
                    />
                ))}
            </GoogleMapReact>
        </div>
    );
};

export default MultiVehicleMap;
