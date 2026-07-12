import { createRouter, createWebHistory } from "vue-router";

import Home from "../Views/Home.vue";
import Login from "../Views/LoginPage.vue";
import StudentRegister from "../Views/StudentRegister.vue";
import CompanyRegister from "../Views/CompanyRegister.vue";

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/student/register",
    component: StudentRegister,
  },
  {
    path: "/company/register",
    component: CompanyRegister,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
