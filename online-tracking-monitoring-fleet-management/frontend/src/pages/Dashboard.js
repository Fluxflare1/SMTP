




import React from 'react';
import RealTimeMap from '../components/RealTimeMap';

const Dashboard = () => {
    const gpsUpdateInterval = 10000; // Update every 10 seconds

    return (
        <div>
            <h1>Fleet Management Dashboard</h1>
            <RealTimeMap updateInterval={gpsUpdateInterval} />
        </div>
    );
};

export default Dashboard;






import React from 'react';
import RealTimeMap from '../components/RealTimeMap';

const Dashboard = () => {
    return (
        <div>
            <h1>Fleet Management Dashboard</h1>
            <RealTimeMap />
        </div>
    );
};

export default Dashboard;
