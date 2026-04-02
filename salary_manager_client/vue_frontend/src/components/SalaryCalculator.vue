<template>
  <div>
    <div class="header-row">
      <h2>Hitung Gaji Karyawan</h2>
    </div>

    <div class="form-box">
      <div class="form-grid">
        <div>
          <label>Karyawan</label>
          <select v-model="form.employee_id">
            <option value="" disabled>Pilih karyawan...</option>
            <option v-for="emp in employees" :key="emp.id" :value="emp.id">
              {{ emp.name }} — {{ emp.position }}
            </option>
          </select>
        </div>
        <div>
          <label>Jam Lembur</label>
          <input v-model.number="form.overtime_hours" type="number" min="0" placeholder="0" />
        </div>
        <div>
          <label>Bonus (Rp)</label>
          <input v-model.number="form.bonus" type="number" min="0" placeholder="0" />
        </div>
        <div>
          <label>Potongan (Rp)</label>
          <input v-model.number="form.deduction" type="number" min="0" placeholder="0" />
        </div>
        <div>
          <label>Periode (YYYY-MM)</label>
          <input v-model="form.period_month" placeholder="2026-04" />
        </div>
      </div>
      <button class="btn-primary" :disabled="loading" @click="calculate">
        {{ loading ? "Menghitung..." : "Hitung Gaji" }}
      </button>
    </div>

    <p v-if="error" class="error">{{ error }}</p>

    <div v-if="result" class="result-box">
      <h3>Slip Gaji — {{ result.employee_name }} ({{ result.period }})</h3>
      <div class="result-grid">
        <div class="result-item">
          <span>Gaji Pokok</span>
          <span>Rp {{ fmt(result.base_salary) }}</span>
        </div>
        <div class="result-item">
          <span>Tunjangan</span>
          <span>Rp {{ fmt(result.allowance) }}</span>
        </div>
        <div class="result-item">
          <span>Lembur</span>
          <span>Rp {{ fmt(result.overtime_pay) }}</span>
        </div>
        <div class="result-item">
          <span>Bonus</span>
          <span>Rp {{ fmt(result.bonus) }}</span>
        </div>
        <div class="result-item">
          <span>Gaji Kotor</span>
          <span>Rp {{ fmt(result.gross_salary) }}</span>
        </div>
        <div class="result-item">
          <span>Pajak</span>
          <span>- Rp {{ fmt(result.tax_amount) }}</span>
        </div>
        <div class="result-item">
          <span>Potongan</span>
          <span>- Rp {{ fmt(result.deduction) }}</span>
        </div>
        <div class="result-item">
          <span><strong>Gaji Bersih</strong></span>
          <span><strong>Rp {{ fmt(result.net_salary) }}</strong></span>
        </div>
      </div>
      <a
        :href="pdfUrl"
        target="_blank"
        style="display: inline-block; margin-top: 14px; color: #1a73e8; font-size: 0.9rem"
      >
        📄 Download PDF
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { getEmployees, calculateSalary, getSalarySlipPdfUrl } from "../api/salaryApi.js";

const employees = ref([]);
const loading = ref(false);
const error = ref("");
const result = ref(null);

const form = ref({
  employee_id: "",
  overtime_hours: 0,
  bonus: 0,
  deduction: 0,
  period_month: new Date().toISOString().slice(0, 7),
});

const pdfUrl = computed(() =>
  result.value ? getSalarySlipPdfUrl(result.value.employee_id) : ""
);

const fmt = (val) => Number(val).toLocaleString("id-ID");

async function fetchEmployees() {
  try {
    const res = await getEmployees();
    employees.value = res.data;
  } catch {
    error.value = "Gagal memuat daftar karyawan.";
  }
}

async function calculate() {
  if (!form.value.employee_id) {
    error.value = "Pilih karyawan terlebih dahulu.";
    return;
  }
  loading.value = true;
  error.value = "";
  result.value = null;
  try {
    const res = await calculateSalary(form.value);
    result.value = res.data;
  } catch {
    error.value = "Gagal menghitung gaji. Pastikan data valid.";
  } finally {
    loading.value = false;
  }
}

onMounted(fetchEmployees);
</script>
