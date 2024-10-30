// frontend/src/App.js

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RealTimeVehicleStatus from './components/RealTimeVehicleStatus';

function App() {
    return (
        <Router>
            <Routes>
                {/* Other routes */}
                <Route path="/real-time-vehicle-status" element={<RealTimeVehicleStatus />} />
            </Routes>
        </Router>
    );
}

export default App;
