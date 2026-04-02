<template>
  <div class="mt-6 bg-white border border-green-200 rounded-xl shadow-sm overflow-hidden">
    <!-- Header -->
    <div class="bg-green-50 px-6 py-4 border-b border-green-200">
      <h3 class="font-semibold text-green-800 text-base">Slip Gaji — {{ slip.employee_name }}</h3>
      <p class="text-xs text-green-600 mt-0.5">Periode: {{ slip.period }}</p>
    </div>
    <!-- Body -->
    <div class="p-6">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
        <!-- Komponen gaji -->
        <div class="space-y-2">
          <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">Komponen Gaji</p>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Gaji Pokok</span>
            <span class="font-mono text-slate-900">Rp {{ fmt(slip.base_salary) }}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Tunjangan</span>
            <span class="font-mono text-slate-900">Rp {{ fmt(slip.allowance) }}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Lembur</span>
            <span class="font-mono text-slate-900">Rp {{ fmt(slip.overtime_pay) }}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Bonus</span>
            <span class="font-mono text-slate-900">Rp {{ fmt(slip.bonus) }}</span>
          </div>
          <div class="flex justify-between text-sm pt-2 border-t border-slate-100 font-semibold">
            <span class="text-slate-700">Gaji Kotor</span>
            <span class="font-mono text-slate-900">Rp {{ fmt(slip.gross_salary) }}</span>
          </div>
        </div>
        <!-- Potongan -->
        <div class="space-y-2">
          <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-3">Potongan</p>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Pajak</span>
            <span class="font-mono text-red-500">- Rp {{ fmt(slip.tax_amount) }}</span>
          </div>
          <div class="flex justify-between text-sm">
            <span class="text-slate-600">Potongan lain</span>
            <span class="font-mono text-red-500">- Rp {{ fmt(slip.deduction) }}</span>
          </div>
          <div class="flex justify-between items-center pt-3 mt-2 border-t-2 border-green-300">
            <span class="font-bold text-slate-900">Gaji Bersih</span>
            <span class="font-mono font-bold text-green-700 text-lg">Rp {{ fmt(slip.net_salary) }}</span>
          </div>
        </div>
      </div>
      <!-- Download -->
      <div class="mt-5 pt-4 border-t border-slate-100 flex gap-3">
        <a
          :href="previewUrl"
          target="_blank"
          class="inline-flex items-center gap-2 px-4 py-2 bg-white border text-slate-800 text-xs font-medium rounded-lg hover:bg-slate-50 transition-colors"
        >
          👁️ Preview
        </a>
        <a
          :href="downloadUrl"
          target="_blank"
          class="inline-flex items-center gap-2 px-4 py-2 bg-slate-800 text-white text-xs font-medium rounded-lg hover:bg-slate-900 transition-colors"
        >
          📄 Download PDF
        </a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { fmt } from "../../../shared/utils/format.js";

defineProps({
  slip: { type: Object, required: true },
});
const BACKEND_BASE = "http://127.0.0.1:8000"
const previewUrl = `${BACKEND_BASE}/salary/slip/${slip.employee_id}/html`
const downloadUrl = `${BACKEND_BASE}/salary/slip/${slip.employee_id}/pdf`
</script>

