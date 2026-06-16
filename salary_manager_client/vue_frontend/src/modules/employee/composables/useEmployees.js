import { ref } from "vue";
import { storeToRefs } from "pinia";
import { useEmployeeStore } from "../store/employeeStore.js";
import * as service from "../services/employeeService.js";

export function useEmployees() {
  const store = useEmployeeStore();
  const { employees } = storeToRefs(store);

  const loading = ref(false);
  const error = ref("");

  async function loadEmployees() {
    loading.value = true;
    error.value = "";
    try {
      const res = await service.fetchEmployees();
      employees.value = res.data;
    } catch {
      error.value = "Gagal memuat karyawan. Pastikan FastAPI berjalan di http://127.0.0.1:8000";
    } finally {
      loading.value = false;
    }
  }

  async function createEmployee(data) {
    error.value = "";
    try {
      await service.addEmployee(data);
      await loadEmployees();
    } catch {
      error.value = "Gagal menambah karyawan.";
      throw new Error("Gagal menambah karyawan.");
    }
  }

  async function deleteEmployee(id) {
    error.value = "";
    try {
      await service.removeEmployee(id);
      await loadEmployees();
    } catch {
      error.value = "Gagal menghapus karyawan.";
    }
  }

  return { employees, loading, error, loadEmployees, createEmployee, deleteEmployee };
}
