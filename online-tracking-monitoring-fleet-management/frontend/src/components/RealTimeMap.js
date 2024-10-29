





import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import PropTypes from 'prop-types';

const RealTimeMap = ({ updateInterval = 5000 }) => {
    const [vehicleLocations, setVehicleLocations] = useState([]);

    useEffect(() => {
        const fetchGPSData = async () => {
            try {
                const response = await fetch('/api/fleet_management/gps/');
                const data = await response.json();
                setVehicleLocations(data);
            } catch (error) {
                console.error('Error fetching GPS data:', error);
            }
        };

        fetchGPSData();
        const interval = setInterval(fetchGPSData, updateInterval);
        return () => clearInterval(interval);
    }, [updateInterval]);

    const mapCenter = vehicleLocations.length > 0 ? [vehicleLocations[0].latitude, vehicleLocations[0].longitude] : [51.505, -0.09];
    const mapZoom = vehicleLocations.length > 0 ? 12 : 5;

    return (
        <MapContainer center={mapCenter} zoom={mapZoom} style={{ height: '100vh', width: '100%' }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution="&copy; <a href='https://osm.org/copyright'>OpenStreetMap</a> contributors"
            />
            {vehicleLocations.map((location) => (
                <Marker
                    key={location.id}
                    position={[location.latitude, location.longitude]}
                    icon={L.icon({
                        iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
                        iconSize: [25, 41],
                        iconAnchor: [12, 41],
                    })}
                >
                    <Popup>
                        <strong>Vehicle ID:</strong> {location.vehicle} <br />
                        <strong>Timestamp:</strong> {new Date(location.timestamp).toLocaleString()}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

RealTimeMap.propTypes = {
    updateInterval: PropTypes.number,
};

export default RealTimeMap;






import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

const RealTimeMap = () => {
    const [vehicleLocations, setVehicleLocations] = useState([]);

    useEffect(() => {
        const fetchGPSData = async () => {
            try {
                const response = await fetch('/api/fleet_management/gps/');
                const data = await response.json();
                setVehicleLocations(data);
            } catch (error) {
                console.error('Error fetching GPS data:', error);
            }
        };

        // Fetch data every 5 seconds
        fetchGPSData();
        const interval = setInterval(fetchGPSData, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '100vh', width: '100%' }}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution="&copy; <a href='https://osm.org/copyright'>OpenStreetMap</a> contributors"
            />
            {vehicleLocations.map((location) => (
                <Marker
                    key={location.id}
                    position={[location.latitude, location.longitude]}
                    icon={L.icon({
                        iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
                        iconSize: [38, 95],
                    })}
                >
                    <Popup>
                        Vehicle: {location.vehicle} <br /> Timestamp: {new Date(location.timestamp).toLocaleString()}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

export default RealTimeMap;
