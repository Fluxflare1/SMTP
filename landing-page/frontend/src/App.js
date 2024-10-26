// App.js
import React from 'react';
import HeroSection from './components/HeroSection';
import ProductOverview from './components/ProductOverview';
import ServicesOverview from './components/ServicesOverview';
import PricingSection from './components/PricingSection';
import DemoSection from './components/DemoSection';
import NewsletterSignup from './components/NewsletterSignup';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <HeroSection />
      <ProductOverview />
      <ServicesOverview />
      <PricingSection />
      <DemoSection />
      <NewsletterSignup />
      <Footer />
    </div>
  );
}

export default App;
