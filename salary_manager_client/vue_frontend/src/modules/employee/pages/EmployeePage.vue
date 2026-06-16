<template>
  <div>
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-xl font-bold text-slate-900">Daftar Karyawan</h1>
        <p class="text-sm text-slate-500 mt-0.5">Kelola data karyawan perusahaan</p>
      </div>
      <button
        class="px-4 py-2 rounded-lg text-sm font-medium transition-colors"
        :class="showForm ? 'bg-slate-200 text-slate-700 hover:bg-slate-300' : 'bg-blue-600 text-white hover:bg-blue-700'"
        @click="showForm = !showForm"
      >
        {{ showForm ? "✕ Batal" : "+ Tambah Karyawan" }}
      </button>
    </div>

    <div v-if="error" class="flex items-center gap-2 text-sm text-red-700 bg-red-50 border border-red-200 rounded-xl px-4 py-3 mb-4">
      <span>⚠</span> {{ error }}
    </div>

    <EmployeeForm v-if="showForm" @submit="handleCreate" />

    <div v-if="loading" class="bg-white border border-slate-200 rounded-xl p-12 text-center shadow-sm">
      <p class="text-slate-400 text-sm">Memuat data...</p>
    </div>

    <EmployeeTable v-if="!loading" :employees="employees" @delete="handleDelete" />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import EmployeeForm from "../components/EmployeeForm.vue";
import EmployeeTable from "../components/EmployeeTable.vue";
import { useEmployees } from "../composables/useEmployees.js";

const { employees, loading, error, loadEmployees, createEmployee, deleteEmployee } = useEmployees();
const showForm = ref(false);

async function handleCreate(data) {
  try {
    await createEmployee(data);
    showForm.value = false;
  } catch {
    // error sudah di-set di composable
  }
}

async function handleDelete(id) {
  if (!confirm("Hapus karyawan ini?")) return;
  await deleteEmployee(id);
}

onMounted(loadEmployees);
</script>
