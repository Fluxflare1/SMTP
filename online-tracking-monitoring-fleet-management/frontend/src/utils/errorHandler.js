// Centralized error handler for API calls
const errorHandler = (error) => {
  const { response } = error;
  if (response) {
    // Server error
    alert(`Error: ${response.data.message}`);
  } else {
    // Network or other error
    alert("Network error. Please check your connection.");
  }
};

export default errorHandler;
