import { ref, computed } from "vue";
import { storeToRefs } from "pinia";
import { useSalaryStore } from "../store/salaryStore.js";
import * as service from "../services/salaryService.js";

export function useSalaryCalculator() {
  const store = useSalaryStore();
  const { lastResult } = storeToRefs(store);

  const loading = ref(false);
  const error = ref("");

  const form = ref({
    employee_id: "",
    overtime_hours: 0,
    bonus: 0,
    deduction: 0,
    period_month: new Date().toISOString().slice(0, 7),
  });

  const pdfUrl = computed(() =>
    lastResult.value ? service.getSalarySlipPdfUrl(lastResult.value.employee_id) : ""
  );

  async function calculate() {
    if (!form.value.employee_id) {
      error.value = "Pilih karyawan terlebih dahulu.";
      return;
    }
    loading.value = true;
    error.value = "";
    lastResult.value = null;
    try {
      const res = await service.postCalculateSalary(form.value);
      lastResult.value = res.data;
    } catch {
      error.value = "Gagal menghitung gaji. Pastikan data valid.";
    } finally {
      loading.value = false;
    }
  }

  return { form, lastResult, loading, error, pdfUrl, calculate };
}
