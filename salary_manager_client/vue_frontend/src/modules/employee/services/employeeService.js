import axios from "axios";

const api = axios.create({ baseURL: "http://127.0.0.1:8000" });

export const fetchEmployees = () => api.get("/employees");
export const addEmployee = (data) => api.post("/employees", data);
export const removeEmployee = (id) => api.delete(`/employees/${id}`);
