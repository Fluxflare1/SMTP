import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/dashboard">Dashboard</Link></li>
                <li><Link to="/schedule-trip">Schedule Trip</Link></li>
                <li><Link to="/assign-vehicle">Assign Vehicle</Link></li>
                <li><Link to="/optimize-route">Optimize Route</Link></li>
            </ul>
        </nav>
    );
};

export default Sidebar;
