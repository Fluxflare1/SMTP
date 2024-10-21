import React from 'react';
import VehicleList from './components/VehicleList';
import DriverList from './components/DriverList';
import TripList from './components/TripList';
import './styles/App.css';

function App() {
  return (
    <div className="App">
      <h1>Dispatcher Panel</h1>
      <VehicleList />
      <DriverList />
      <TripList />
    </div>
  );
}

export default App;
