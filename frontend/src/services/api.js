import axios from 'axios';

const API_BASE_URL = "http://127.0.0.1:8000";

export const analyzeUser = async (username) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/analyze/${username}`);
    return response.data;
  } catch (error) {
    console.error("API Call Failed:", error);
    return { error: "Backend unreachable" };
  }
};