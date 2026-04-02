import axios from "axios";

const api = axios.create({ baseURL: "http://127.0.0.1:8000" });

export const postCalculateSalary = (data) => api.post("/salary/calculate", data);
export const fetchSalarySlips = (month = null) =>
  api.get("/salary/slips", { params: month ? { month } : {} });
export const getSalarySlipPdfUrl = (employeeId) =>
  `http://127.0.0.1:8000/salary/slip/${employeeId}/pdf`;
