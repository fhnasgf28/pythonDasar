import { defineStore } from "pinia";
import { ref } from "vue";

export const useSalaryStore = defineStore("salary", () => {
  const slips = ref([]);
  const lastResult = ref(null);
  return { slips, lastResult };
});
