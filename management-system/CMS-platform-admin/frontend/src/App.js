import React from 'react';
import HeroSection from './components/HeroSection';
import GlobalServices from './components/GlobalServices';
import TenantServices from './components/TenantServices';
import PlatformFeatures from './components/PlatformFeatures';
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
