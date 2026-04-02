<template>
  <div class="min-h-screen bg-slate-50">
    <!-- Navbar -->
    <header class="bg-white border-b border-slate-200 shadow-sm sticky top-0 z-10">
      <div class="max-w-6xl mx-auto px-4 sm:px-6">
        <div class="flex items-center justify-between h-16">
          <!-- Logo -->
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 bg-blue-600 rounded-xl flex items-center justify-center shadow-sm">
              <span class="text-white font-bold text-xs">Rp</span>
            </div>
            <div>
              <p class="font-semibold text-slate-900 text-sm leading-none">Salary Manager</p>
              <p class="text-xs text-slate-400 mt-0.5">v3.0.0</p>
            </div>
          </div>
          <!-- Nav links -->
          <nav class="flex gap-1">
            <router-link to="/employees" class="nav-link px-4 py-2 rounded-lg text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors">
              Karyawan
            </router-link>
            <router-link to="/salary/calculator" class="nav-link px-4 py-2 rounded-lg text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors">
              Hitung Gaji
            </router-link>
            <router-link to="/salary/slips" class="nav-link px-4 py-2 rounded-lg text-sm font-medium text-slate-600 hover:bg-slate-100 hover:text-slate-900 transition-colors">
              Slip Gaji
            </router-link>
          </nav>
        </div>
      </div>
    </header>

    <main class="max-w-6xl mx-auto px-4 sm:px-6 py-8">
      <router-view />
    </main>
  </div>
</template>

<script setup>
// Layout only — routing ditangani oleh Vue Router
</script>
