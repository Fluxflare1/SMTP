import React, { useState } from 'react';
import './Faq.css';

const Faq = () => {
  const [activeIndex, setActiveIndex] = useState(null);

  const toggleFaq = (index) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  return (
    <section className="faq-section">
      <h2>Frequently Asked Questions</h2>
      <div className="faq-container">
        <div className="faq-item" onClick={() => toggleFaq(0)}>
          <h3>What is the platform about?</h3>
          {activeIndex === 0 && <p>Our platform provides global and local transportation services with white-label solutions for tenants.</p>}
        </div>
        <div className="faq-item" onClick={() => toggleFaq(1)}>
          <h3>How can I manage my fleet?</h3>
          {activeIndex === 1 && <p>You can manage your fleet through our Fleet Management System, which provides real-time tracking and reporting.</p>}
        </div>
        <div className="faq-item" onClick={() => toggleFaq(2)}>
          <h3>How do I sign up?</h3>
          {activeIndex === 2 && <p>Sign up through our platform by providing your details and selecting the services you wish to use.</p>}
        </div>
      </div>
    </section>
  );
};

export default Faq;
