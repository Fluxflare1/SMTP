const getCachedData = (key) => JSON.parse(localStorage.getItem(key));
const setCachedData = (key, data) => localStorage.setItem(key, JSON.stringify(data));

export { getCachedData, setCachedData };
