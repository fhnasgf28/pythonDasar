import { ref } from "vue";
import { storeToRefs } from "pinia";
import { useSalaryStore } from "../store/salaryStore.js";
import * as service from "../services/salaryService.js";

export function useSalarySlips() {
  const store = useSalaryStore();
  const { slips } = storeToRefs(store);

  const loading = ref(false);
  const error = ref("");
  const filterMonth = ref("");

  async function loadSlips() {
    loading.value = true;
    error.value = "";
    try {
      const res = await service.fetchSalarySlips(filterMonth.value || null);
      slips.value = res.data;
    } catch {
      error.value = "Gagal memuat slip gaji. Pastikan FastAPI berjalan di http://127.0.0.1:8000";
    } finally {
      loading.value = false;
    }
  }

  function clearFilter() {
    filterMonth.value = "";
    loadSlips();
  }

  return { slips, loading, error, filterMonth, loadSlips, clearFilter };
}
