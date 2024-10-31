import React from "react";
import { Navigate } from "react-router-dom";
import isAuthenticated from "../utils/auth";

const ProtectedRoute = ({ children, role }) => {
  if (!isAuthenticated()) {
    return <Navigate to="/login" />;
  }
  return children;
};

export default ProtectedRoute;
