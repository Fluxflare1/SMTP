import React from 'react';
import './TenantServices.css';

const TenantServices = () => {
  return (
    <section className="tenant-services">
      <h2>White-Label Solutions for Tenants</h2>
      <p>Run your own branded transportation service with complete flexibility. Customize your service offerings and provide a seamless booking experience for your customers.</p>
      <div className="tenant-features">
        <div className="feature-card">
          <h3>Branding Flexibility</h3>
          <p>Customize the platform to match your brand's look and feel.</p>
        </div>
        <div className="feature-card">
          <h3>Multi-Service Support</h3>
          <p>Offer ride-hailing, shuttle, logistics, and more within one unified platform.</p>
        </div>
        <div className="feature-card">
          <h3>Unified Customer Interface</h3>
          <p>Manage bookings from multiple services in one place.</p>
        </div>
      </div>
    </section>
  );
};

export default TenantServices;
