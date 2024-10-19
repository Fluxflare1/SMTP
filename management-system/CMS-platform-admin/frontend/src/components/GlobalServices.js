import React from 'react';
import './GlobalServices.css';

const GlobalServices = () => {
  return (
    <section className="global-services">
      <h2>Global Transportation Services</h2>
      <p>Book rides from multiple transportation providers worldwide. Our platform offers a unified interface for seamless booking and travel experiences.</p>
      <div className="map-container">
        {/* Add an interactive map or image here */}
        <img src="/assets/world-map.png" alt="Global service map" />
      </div>
    </section>
  );
};

export default GlobalServices;