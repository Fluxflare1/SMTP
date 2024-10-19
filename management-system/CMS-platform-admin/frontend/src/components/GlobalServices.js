import React from 'react';
import './GlobalServices.css';

const GlobalServices = () => {
  return (
    <section className="global-services">
      <h2>Global Transportation Services</h2>
      <p>Book rides from multiple transportation providers worldwide. Our platform offers a unified interface for seamless booking, real-time tracking with GPS devices, and efficient global fleet management.</p>
      <div className="map-container">
        <img src="/assets/world-map.png" alt="Global service map" />
      </div>
    </section>
  );
};

export default GlobalServices;
