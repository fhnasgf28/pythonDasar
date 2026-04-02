<template>
  <div class="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden">
    <div v-if="employees.length">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-slate-200 bg-slate-50">
            <th class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">ID</th>
            <th class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Nama</th>
            <th class="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">Posisi</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Gaji Pokok</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Tunjangan</th>
            <th class="px-4 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">Lembur/jam</th>
            <th class="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider">Pajak</th>
            <th class="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider">Aksi</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-slate-100">
          <tr v-for="emp in employees" :key="emp.id" class="hover:bg-slate-50 transition-colors">
            <td class="px-4 py-3 text-slate-400 font-mono text-xs">#{{ emp.id }}</td>
            <td class="px-4 py-3 font-medium text-slate-900">{{ emp.name }}</td>
            <td class="px-4 py-3">
              <span class="px-2.5 py-1 bg-blue-50 text-blue-700 text-xs rounded-full font-medium">{{ emp.position }}</span>
            </td>
            <td class="px-4 py-3 text-right font-mono text-slate-700">Rp {{ fmt(emp.base_salary) }}</td>
            <td class="px-4 py-3 text-right font-mono text-slate-700">Rp {{ fmt(emp.allowance) }}</td>
            <td class="px-4 py-3 text-right font-mono text-slate-700">Rp {{ fmt(emp.overtime_rate) }}</td>
            <td class="px-4 py-3 text-center">
              <span class="px-2.5 py-1 bg-amber-50 text-amber-700 text-xs rounded-full font-medium">{{ emp.tax_percent }}%</span>
            </td>
            <td class="px-4 py-3 text-center">
              <button @click="emit('delete', emp.id)" class="px-3 py-1 bg-red-50 text-red-600 text-xs font-medium rounded-lg hover:bg-red-100 hover:text-red-700 transition-colors">
                Hapus
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else class="py-16 text-center">
      <div class="text-4xl mb-3">👤</div>
      <p class="text-slate-500 text-sm font-medium">Belum ada karyawan</p>
      <p class="text-slate-400 text-xs mt-1">Tambahkan karyawan baru menggunakan tombol di atas</p>
    </div>
  </div>
</template>

<script setup>
import { fmt } from "../../../shared/utils/format.js";

defineProps({ employees: { type: Array, required: true } });
const emit = defineEmits(["delete"]);
</script>

