import React from 'react';
import HeroSection from './components/HeroSection';
import GlobalServices from './components/GlobalServices';
import TenantServices from './components/TenantServices';
import PlatformFeatures from './components/PlatformFeatures';
import Products from './components/Products';  // New Products Component
import Services from './components/Services';  // New Services Component
import HowItWorks from './components/HowItWorks';
import Testimonials from './components/Testimonials';
import PricingPlans from './components/PricingPlans';
import Faq from './components/Faq';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <HeroSection />
      <GlobalServices />
      <TenantServices />
      <Products />   {/* Insert Products Component */}
      <Services />   {/* Insert Services Component */}
      <PlatformFeatures />
      <HowItWorks />
      <Testimonials />
      <PricingPlans />
      <Faq />
      <Footer />
    </div>
  );
}

export default App;
