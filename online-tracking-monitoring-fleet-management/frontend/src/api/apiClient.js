import axios from "axios";
import errorHandler from "../utils/errorHandler";

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    errorHandler(error);
    return Promise.reject(error);
  }
);

export default apiClient;
