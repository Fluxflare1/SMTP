import React, { useEffect } from 'react';

const TrackingMap = () => {
    useEffect(() => {
        const map = new google.maps.Map(document.getElementById('map'), {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8,
        });

        const trafficLayer = new google.maps.TrafficLayer();
        trafficLayer.setMap(map);
    }, []);

    return (
        <div id="map" style={{ height: '500px', width: '100%' }}></div>
    );
};

export default TrackingMap;
