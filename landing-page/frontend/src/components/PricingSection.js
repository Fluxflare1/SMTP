
// Example: Wrapping the PricingSection with animation
import { Fade } from 'react-scroll-reveal';

function PricingSection() {
  return (
    <Fade>
      <section className="pricing-section">
        <h2>Flexible Pricing Plans</h2>
        ...
      </section>
    </Fade>
  );
}



// PricingSection.js
import React from 'react';
import './PricingSection.css';

function PricingSection() {
  return (
    <section className="pricing-section">
      <h2>Flexible Pricing Plans</h2>
      <div className="pricing-tiers">
        <div className="tier">
          <h3>Basic</h3>
          <p>$99/month</p>
          <ul>
            <li>Fleet Tracking</li>
            <li>Basic Reporting</li>
            <li>Email Support</li>
          </ul>
          <button className="btn-primary">Choose Basic</button>
        </div>
        <div className="tier">
          <h3>Pro</h3>
          <p>$199/month</p>
          <ul>
            <li>Advanced Analytics</li>
            <li>24/7 Support</li>
            <li>API Access</li>
          </ul>
          <button className="btn-primary">Choose Pro</button>
        </div>
        <div className="tier">
          <h3>Enterprise</h3>
          <p>Contact Us</p>
          <ul>
            <li>Custom Integrations</li>
            <li>Dedicated Support</li>
            <li>White-Label Options</li>
          </ul>
          <button className="btn-primary">Contact Sales</button>
        </div>
      </div>
    </section>
  );
}

export default PricingSection;
