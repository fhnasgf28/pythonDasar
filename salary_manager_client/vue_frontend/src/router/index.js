import { createRouter, createWebHashHistory } from "vue-router";
import EmployeePage from "../modules/employee/pages/EmployeePage.vue";
import SalaryCalculatorPage from "../modules/salary/pages/SalaryCalculatorPage.vue";
import SalarySlipsPage from "../modules/salary/pages/SalarySlipsPage.vue";

const routes = [
  { path: "/", redirect: "/employees" },
  { path: "/employees", component: EmployeePage },
  { path: "/salary/calculator", component: SalaryCalculatorPage },
  { path: "/salary/slips", component: SalarySlipsPage },
];

export default createRouter({
  history: createWebHashHistory(),
  routes,
});
