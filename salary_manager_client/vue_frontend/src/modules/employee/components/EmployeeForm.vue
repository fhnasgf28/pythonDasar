<template>
  <div class="bg-white border border-slate-200 rounded-xl p-6 mb-6 shadow-sm">
    <h3 class="text-base font-semibold text-slate-800 mb-4">Data Karyawan Baru</h3>
    <div v-if="localError" class="flex items-center gap-2 text-sm text-red-700 bg-red-50 border border-red-200 rounded-lg px-3 py-2.5 mb-4">
      <span>⚠</span> {{ localError }}
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-5">
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Nama <span class="text-red-500">*</span></label>
        <input v-model="form.name" placeholder="Nama lengkap" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Posisi / Jabatan <span class="text-red-500">*</span></label>
        <input v-model="form.position" placeholder="Backend Developer" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Gaji Pokok (Rp)</label>
        <input v-model.number="form.base_salary" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Tunjangan (Rp)</label>
        <input v-model.number="form.allowance" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Tarif Lembur/jam (Rp)</label>
        <input v-model.number="form.overtime_rate" type="number" min="0" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-600 mb-1.5">Pajak (%)</label>
        <input v-model.number="form.tax_percent" type="number" min="0" max="100" step="0.1" placeholder="0" class="w-full px-3 py-2 text-sm border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow" />
      </div>
    </div>
    <button @click="handleSubmit" class="px-5 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 active:bg-blue-800 transition-colors">
      Simpan Karyawan
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["submit"]);

const defaultForm = () => ({
  name: "",
  position: "",
  base_salary: 0,
  allowance: 0,
  overtime_rate: 0,
  tax_percent: 0,
});

const form = ref(defaultForm());
const localError = ref("");

function handleSubmit() {
  if (!form.value.name.trim() || !form.value.position.trim()) {
    localError.value = "Nama dan posisi wajib diisi.";
    return;
  }
  localError.value = "";
  emit("submit", { ...form.value });
  form.value = defaultForm();
}
</script>

