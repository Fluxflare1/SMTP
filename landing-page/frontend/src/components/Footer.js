// Footer.js
import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <p>&copy; 2024 Flux Transportation Services. All rights reserved.</p>
      <ul className="footer-links">
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#demo">Book a Demo</a></li>
        <li><a href="#login">Login</a></li>
        <li><a href="#signup">Signup</a></li>
      </ul>
    </footer>
  );
}

export default Footer;
