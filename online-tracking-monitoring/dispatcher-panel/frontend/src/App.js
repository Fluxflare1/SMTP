import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TripSchedule from './components/TripSchedule';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/schedule-trip" element={<TripSchedule />} />
            </Routes>
        </Router>
    );
}

export default App;
