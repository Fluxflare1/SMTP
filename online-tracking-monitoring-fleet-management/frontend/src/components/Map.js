import { GoogleMap, LoadScript, Marker } from "@react-google-maps/api";

const Map = ({ locations }) => (
  <LoadScript googleMapsApiKey="YOUR_GOOGLE_MAPS_API_KEY">
    <GoogleMap mapContainerStyle={{ height: "400px", width: "100%" }} zoom={10}>
      {locations.map((loc, index) => (
        <Marker key={index} position={{ lat: loc.lat, lng: loc.lng }} />
      ))}
    </GoogleMap>
  </LoadScript>
);

export default Map;
