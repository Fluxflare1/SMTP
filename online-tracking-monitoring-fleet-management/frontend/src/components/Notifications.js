import React, { useEffect, useState } from 'react';
import { getNotifications } from '../services/api';

const Notifications = ({ userId }) => {
    const [notifications, setNotifications] = useState([]);

    useEffect(() => {
        const fetchNotifications = async () => {
            const res = await getNotifications(userId);
            setNotifications(res.data);
        };

        fetchNotifications();
    }, [userId]);

    return (
        <ul>
            {notifications.map((notification, index) => (
                <li key={index}>{notification.message}</li>
            ))}
        </ul>
    );
};

export default Notifications;
