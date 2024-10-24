



import React from 'react';
import './HeroSection.css';

const HeroSection = () => {
  return (
    <section className="hero-section" aria-labelledby="hero-heading">
      <div className="hero-content">
        <h1 id="hero-heading">Unifying Transportation Globally</h1>
        <p>
          Power your transportation services with our multi-modal, white-label platform offering global and local solutions.
        </p>
        <div className="cta-buttons">
          <button className="btn primary-btn" aria-label="Get started with SMTP">Get Started</button>
          <button className="btn secondary-btn" aria-label="Explore services offered by SMTP">Explore Services</button>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;






import React from 'react';
import './HeroSection.css';

const HeroSection = () => {
  return (
    <section className="hero-section">
      <div className="hero-content">
        <h1>Unifying Transportation Globally</h1>
        <p>Power your transportation services with our multi-modal, white-label platform offering global and local solutions.</p>
        <div className="cta-buttons">
          <button className="btn primary-btn">Get Started</button>
          <button className="btn secondary-btn">Explore Services</button>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
