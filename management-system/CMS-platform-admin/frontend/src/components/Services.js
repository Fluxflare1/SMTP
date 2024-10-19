import React from 'react';
import './Services.css';

const Services = () => {
  return (
    <section className="services">
      <h2>Our Services</h2>
      <div className="service-list">
        <div className="service-card">
          <h3>Software Development</h3>
          <p>Custom software solutions designed to meet the needs of your transportation business.</p>
        </div>
        <div className="service-card">
          <h3>Software as a Service (SaaS)</h3>
          <p>Leverage our powerful SaaS platform to manage transportation services with ease.</p>
        </div>
        <div className="service-card">
          <h3>Sales and Installation of GPS Tracking Devices</h3>
          <p>We provide high-quality GPS tracking devices and professional installation services.</p>
        </div>
      </div>
    </section>
  );
};

export default Services;
