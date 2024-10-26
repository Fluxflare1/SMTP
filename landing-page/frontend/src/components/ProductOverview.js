


// ProductOverview.js
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTruck, faMapMarkedAlt, faGasPump } from '@fortawesome/free-solid-svg-icons';

function ProductOverview() {
  return (
    <section className="product-overview">
      <h2>Our Products</h2>
      <div className="product-item">
        <FontAwesomeIcon icon={faMapMarkedAlt} /> Online Tracking, Monitoring & Fleet Management
      </div>
      <div className="product-item">
        <FontAwesomeIcon icon={faTruck} /> Global Transportation Services
      </div>
      ...
    </section>
  );
}



// ProductOverview.js
import React from 'react';
import './ProductOverview.css';

function ProductOverview() {
  return (
    <section className="product-overview">
      <h2>Our SaaS Solutions for Transportation Providers</h2>
      <ul>
        <li><strong>Online Tracking, Monitoring & Fleet Management</strong>: Real-time insights for managing fleets efficiently.</li>
        <li><strong>Global Transportation Services</strong>: Unified booking and service management.</li>
        <li><strong>Transportation Services Management</strong>: Modules for ride-hailing, shuttles, and more.</li>
        <li><strong>Inspection Agent Portal</strong>: Manage and track inspections easily.</li>
        <li><strong>GPS Tracker Solutions</strong>: Reliable tracking for vehicles and assets.</li>
        <li><strong>CNG Kits and Retrofitting</strong>: High-quality CNG retrofit services.</li>
      </ul>
    </section>
  );
}

export default ProductOverview;
