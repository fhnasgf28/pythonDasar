<template>
  <div>
    <div class="mb-6">
      <h1 class="text-xl font-bold text-slate-900">Hitung Gaji Karyawan</h1>
      <p class="text-sm text-slate-500 mt-0.5">Masukkan data untuk menghitung slip gaji</p>
    </div>

    <div class="bg-white border border-slate-200 rounded-xl shadow-sm p-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-5">
        <div class="sm:col-span-2 lg:col-span-1">
          <label class="block text-xs font-medium text-slate-600 mb-1.5">Karyawan</label>
          <select v-model="form.employee_id" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white">
            <option value="" disabled>Pilih karyawan...</option>
            <option v-for="emp in employees" :key="emp.id" :value="emp.id">
              {{ emp.name }} — {{ emp.position }}
            </option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-medium text-slate-600 mb-1.5">Jam Lembur</label>
          <input v-model.number="form.overtime_hours" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
        </div>
        <div>
          <label class="block text-xs font-medium text-slate-600 mb-1.5">Bonus (Rp)</label>
          <input v-model.number="form.bonus" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
        </div>
        <div>
          <label class="block text-xs font-medium text-slate-600 mb-1.5">Potongan (Rp)</label>
          <input v-model.number="form.deduction" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
        </div>
        <div>
          <label class="block text-xs font-medium text-slate-600 mb-1.5">Periode (YYYY-MM)</label>
          <input v-model="form.period_month" placeholder="2026-04" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
        </div>
      </div>
      <button
        class="px-5 py-2 rounded-lg text-sm font-medium transition-colors"
        :class="loading ? 'bg-slate-200 text-slate-500 cursor-not-allowed' : 'bg-blue-600 text-white hover:bg-blue-700'"
        :disabled="loading"
        @click="calculate"
      >
        {{ loading ? "Menghitung..." : "Hitung Gaji" }}
      </button>
    </div>

    <div v-if="error" class="flex items-center gap-2 text-sm text-red-700 bg-red-50 border border-red-200 rounded-xl px-4 py-3 mt-4">
      <span>⚠</span> {{ error }}
    </div>

    <SalaryResultCard v-if="lastResult" :slip="lastResult" :pdf-url="pdfUrl" />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import SalaryResultCard from "../components/SalaryResultCard.vue";
import { useSalaryCalculator } from "../composables/useSalaryCalculator.js";
import { useEmployees } from "../../employee/composables/useEmployees.js";

const { form, lastResult, loading, error, pdfUrl, calculate } = useSalaryCalculator();
const { employees, loadEmployees } = useEmployees();

onMounted(() => {
  if (!employees.value.length) loadEmployees();
});
</script>
