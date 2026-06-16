import { defineStore } from "pinia";
import { ref } from "vue";

export const useEmployeeStore = defineStore("employee", () => {
  const employees = ref([]);
  return { employees };
});
