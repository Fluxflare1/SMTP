import React from 'react';
import './Testimonials.css';

const Testimonials = () => {
  return (
    <section className="testimonials">
      <h2>What Our Clients Say</h2>
      <div className="testimonials-container">
        <div className="testimonial">
          <p>"The platform revolutionized how we manage our fleet. The real-time tracking is a game-changer!"</p>
          <h3>- John Doe, Fleet Manager</h3>
        </div>
        <div className="testimonial">
          <p>"The white-label solution allowed us to customize the platform and launch our own transportation service easily."</p>
          <h3>- Jane Smith, CEO of Transport Co.</h3>
        </div>
      </div>
    </section>
  );
};

export default Testimonials;
