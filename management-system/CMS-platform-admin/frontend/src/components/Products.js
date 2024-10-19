import React from 'react';
import './Products.css';

const Products = () => {
  return (
    <section className="products">
      <h2>Our Products</h2>
      <div className="product-list">
        <div className="product-card">
          <h3>Transportation Services Management Systems</h3>
          <p>Manage all transportation services efficiently with our comprehensive management system.</p>
        </div>
        <div className="product-card">
          <h3>Online Tracking and Monitoring System</h3>
          <p>Real-time tracking and monitoring for fleets, ensuring timely and efficient transportation services.</p>
        </div>
        <div className="product-card">
          <h3>Fleet Management System</h3>
          <p>Keep your fleet in optimal condition, track vehicle performance, and schedule maintenance.</p>
        </div>
        <div className="product-card">
          <h3>Vehicle Inspection Agent Portal</h3>
          <p>Streamline vehicle inspection processes with our user-friendly agent portal.</p>
        </div>
        <div className="product-card">
          <h3>GPS Tracking Devices</h3>
          <p>Track your vehicles anywhere, anytime with reliable GPS devices integrated into our platform.</p>
        </div>
      </div>
    </section>
  );
};

export default Products;
