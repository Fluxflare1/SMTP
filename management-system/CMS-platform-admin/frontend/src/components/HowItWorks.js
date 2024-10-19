import React from 'react';
import './HowItWorks.css';

const HowItWorks = () => {
  return (
    <section className="how-it-works">
      <h2>How It Works</h2>
      <div className="steps-container">
        <div className="step">
          <h3>Step 1: Sign Up</h3>
          <p>Create an account with our platform to get started.</p>
        </div>
        <div className="step">
          <h3>Step 2: Choose Services</h3>
          <p>Select the transportation services that best suit your needs.</p>
        </div>
        <div className="step">
          <h3>Step 3: Manage and Track</h3>
          <p>Use our unified platform to manage bookings and track your fleet in real-time.</p>
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;
