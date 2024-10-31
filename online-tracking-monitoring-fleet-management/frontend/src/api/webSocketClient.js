const ws = new WebSocket("wss://your-backend-websocket-url.com");

ws.onopen = () => {
  console.log("Connected to WebSocket");
};

ws.onmessage = (message) => {
  console.log("Received data:", message.data);
  // Handle real-time data updates here
};

export default ws;
