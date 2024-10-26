
import React from 'react';
import HeroSection from './components/HeroSection';
import ProductOverview from './components/ProductOverview';
import ServicesOverview from './components/ServicesOverview';
import PricingSection from './components/PricingSection';
import DemoSection from './components/DemoSection';
import NewsletterSignup from './components/NewsletterSignup';
import Testimonials from './components/Testimonials';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <HeroSection />
      <ProductOverview />
      <ServicesOverview />
      <PricingSection />
      <DemoSection />
      <Testimonials />
      <NewsletterSignup />
      <Footer />
    </div>
  );
}

export default App;




import React, { useEffect } from 'react';
import ReactGA from 'react-ga';

ReactGA.initialize('YOUR-GA-TRACKING-ID');

function App() {
  useEffect(() => {
    ReactGA.pageview(window.location.pathname + window.location.search);
  }, []);

  return (
    <div className="App">
      {/* Components */}
    </div>
  );
}



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
