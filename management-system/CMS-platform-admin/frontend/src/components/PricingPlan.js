import React from 'react';
import './PricingPlans.css';

const PricingPlans = () => {
  return (
    <section className="pricing-plans">
      <h2>Our Pricing Plans</h2>
      <div className="plans-container">
        <div className="plan">
          <h3>Basic</h3>
          <p>$49/month</p>
          <p>Includes basic features such as fleet management and tracking.</p>
          <button className="btn">Get Started</button>
        </div>
        <div className="plan">
          <h3>Pro</h3>
          <p>$99/month</p>
          <p>Includes all basic features plus additional services like white-label customization.</p>
          <button className="btn">Get Started</button>
        </div>
        <div className="plan">
          <h3>Enterprise</h3>
          <p>Contact Us</p>
          <p>Custom solutions tailored to your business needs.</p>
          <button className="btn">Contact Sales</button>
        </div>
      </div>
    </section>
  );
};

export default PricingPlans;
