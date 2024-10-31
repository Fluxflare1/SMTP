const isAuthenticated = () => {
  return Boolean(localStorage.getItem("authToken"));
};

export default isAuthenticated;
