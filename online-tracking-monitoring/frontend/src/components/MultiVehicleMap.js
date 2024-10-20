
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MultiVehicleMap() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    axios.get('/api/get-all-vehicles-data/')
      .then(response => {
        setVehicles(response.data.vehicles);
      })
      .catch(error => {
        console.log('Error fetching vehicle data:', error);
      });
  }, []);

  return (
    <div>
      <h3>Multi-Vehicle View</h3>
      <div id="map" style={{ height: '500px', width: '100%' }}></div>
      
      <script>
        function initMap() {
          const map = new google.maps.Map(document.getElementById('map'), {
            zoom: 8,
            center: { lat: 10.123, lng: 12.456 } // Default center, can update dynamically
          });

          const vehicles = {JSON.stringify(vehicles)};

          vehicles.forEach(vehicle => {
            const marker = new google.maps.Marker({
              position: { lat: vehicle.latitude, lng: vehicle.longitude },
              map: map,
              title: `Vehicle ID: ${vehicle.vehicle_id}, Status: ${vehicle.immobilized ? 'Immobilized' : 'Active'}`
            });
          });
        }

        window.initMap = initMap;
      </script>

      <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_GOOGLE_MAPS_API_KEY&callback=initMap"
              async defer></script>
    </div>
  );
}

export default MultiVehicleMap;






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
