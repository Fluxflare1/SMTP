// NewsletterSignup.js
import React, { useState } from 'react';
import './NewsletterSignup.css';

function NewsletterSignup() {
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Subscribed:', email);
  };

  return (
    <section className="newsletter-signup">
      <h2>Stay Updated on Transportation Technology</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit" className="btn-primary">Subscribe</button>
      </form>
    </section>
  );
}

export default NewsletterSignup;
