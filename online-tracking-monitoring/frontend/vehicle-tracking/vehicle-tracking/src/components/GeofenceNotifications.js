import React, { useEffect, useState } from 'react';

const GeofenceNotifications = () => {
    const [messages, setMessages] = useState([]);

    useEffect(() => {
        const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

        socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setMessages((prevMessages) => [...prevMessages, data.message]);
        };

        socket.onclose = (event) => {
            console.log('WebSocket connection closed', event);
        };

        return () => {
            socket.close();
        };
    }, []);

    return (
        <div>
            <h2>Real-time Geofence Notifications</h2>
            <ul>
                {messages.map((message, index) => (
                    <li key={index}>{message}</li>
                ))}
            </ul>
        </div>
    );
};

export default GeofenceNotifications;
