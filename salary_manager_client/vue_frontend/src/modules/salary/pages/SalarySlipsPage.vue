<template>
  <div>
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-xl font-bold text-slate-900">Riwayat Slip Gaji</h1>
        <p class="text-sm text-slate-500 mt-0.5">Semua slip gaji yang telah diterbitkan</p>
      </div>
      <div class="flex gap-2 items-center">
        <input
          v-model="filterMonth"
          placeholder="Filter: 2026-04"
          class="w-36 px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          @keyup.enter="loadSlips"
        />
        <button @click="loadSlips" class="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors">Filter</button>
        <button v-if="filterMonth" @click="clearFilter" class="px-4 py-2 bg-slate-200 text-slate-700 text-sm font-medium rounded-lg hover:bg-slate-300 transition-colors">Reset</button>
      </div>
    </div>

    <div v-if="error" class="flex items-center gap-2 text-sm text-red-700 bg-red-50 border border-red-200 rounded-xl px-4 py-3 mb-4">
      <span>⚠</span> {{ error }}
    </div>

    <div class="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden">
      <div v-if="loading" class="py-16 text-center">
        <p class="text-slate-400 text-sm">Memuat data...</p>
      </div>
      <div v-else-if="slips.length">
        <table class="w-full text-sm">
          <thead>
            <tr class="border-b border-slate-200 bg-slate-50">
              <th class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">ID</th>
              <th class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Karyawan</th>
              <th class="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider">Periode</th>
              <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Gaji Kotor</th>
              <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Pajak</th>
              <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Potongan</th>
              <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Gaji Bersih</th>
              <th class="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider">PDF</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-100">
            <tr v-for="slip in slips" :key="slip.id" class="hover:bg-slate-50 transition-colors">
              <td class="px-4 py-3 text-slate-400 font-mono text-xs">#{{ slip.id }}</td>
              <td class="px-4 py-3 font-medium text-slate-900">{{ slip.employee_name }}</td>
              <td class="px-4 py-3 text-center">
                <span class="px-2.5 py-1 bg-slate-100 text-slate-700 text-xs rounded-full font-mono">{{ slip.period }}</span>
              </td>
              <td class="px-4 py-3 text-right font-mono text-slate-700">Rp {{ fmt(slip.gross_salary) }}</td>
              <td class="px-4 py-3 text-right font-mono text-red-500">- Rp {{ fmt(slip.tax_amount) }}</td>
              <td class="px-4 py-3 text-right font-mono text-red-500">- Rp {{ fmt(slip.deduction) }}</td>
              <td class="px-4 py-3 text-right font-mono font-bold text-green-700">Rp {{ fmt(slip.net_salary) }}</td>
              <td class="px-4 py-3 text-center">
                <div class="inline-flex items-center gap-2">
                  <a :href="`http://127.0.0.1:8000/salary/slip/${slip.employee_id}/html`" target="_blank" class="inline-flex items-center gap-1 px-2.5 py-1 bg-white border text-slate-800 text-xs font-medium rounded-md hover:bg-slate-50 transition-colors">
                    👁️ Preview
                  </a>
                  <a :href="getPdfUrl(slip.employee_id)" target="_blank" class="inline-flex items-center gap-1 px-2.5 py-1 bg-slate-800 text-white text-xs font-medium rounded-md hover:bg-slate-900 transition-colors">
                    📄 PDF
                  </a>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="py-16 text-center">
        <div class="text-4xl mb-3">📄</div>
        <p class="text-slate-500 text-sm font-medium">Belum ada slip gaji</p>
        <p class="text-slate-400 text-xs mt-1">
          {{ filterMonth ? `Tidak ada slip untuk periode ${filterMonth}` : "Hitung gaji untuk membuat slip pertama" }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { fmt } from "../../../shared/utils/format.js";
import { useSalarySlips } from "../composables/useSalarySlips.js";
import { getSalarySlipPdfUrl } from "../services/salaryService.js";

const { slips, loading, error, filterMonth, loadSlips, clearFilter } = useSalarySlips();
const getPdfUrl = getSalarySlipPdfUrl;

onMounted(loadSlips);
</script>
