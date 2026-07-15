import { createRouter, createWebHistory } from "vue-router";

import Home from "../Views/Home.vue";
import Login from "../Views/LoginPage.vue";
import StudentRegister from "../Views/StudentRegister.vue";

import CompanyRegister from "../Views/CompanyRegister.vue";
import AdminDashboard from "../Views/Admin/AdminDashboard.vue";
import CompanyDashboard from "../Views/Company/CompanyDashboard.vue";
import CreateDrive from "../Views/Company/CreateDrive.vue";
import ViewApplicants from "../Views/Company/ViewApplicants.vue";
import StudentDashboard from "../Views/Student/StudentDashboard.vue";
import JobListing from "../Views/Student/JobListing.vue";
import JobDetail from "../Views/Student/JobDetail.vue";
import ApplicationDetail from "../Views/Student/ApplicationDetail.vue";
//import Profile from "../Views/Student/StudentProfile.vue/index.js";
import CompanyDetail from "../Views/Student/CompanyDetail.vue";
import StudentProfile from "@/Views/Student/StudentProfile.vue";
import AdminDriveDetails from "../Views/Admin/AdminDriveDetails.vue";
import AdminApplicationDetails from "../Views/Admin/AdminApplicationDetails.vue";

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
  {
    path: "/admin/dashboard",
    component: AdminDashboard,
    meta: { roles: ["admin"] },
  },
  {
    path: "/company/dashboard",
    component: CompanyDashboard,
    meta: { roles: ["company"] },
  },
  {
    path: "/company/drive/create",
    component: CreateDrive,
  },
  {
    path: "/company/drive/:id/applicants",
    component: ViewApplicants,
  },
  {
    path: "/student/dashboard",
    component: StudentDashboard,
  },
  {
    path: "/student/jobs",
    component: JobListing,
  },
  {
    path: "/student/job/:id",
    component: JobDetail,
  },
  {
    path: "/student/application/:id",
    component: ApplicationDetail,
  },
  {
    path: "/student/profile",
    component: StudentProfile,
  },
  {
    path: "/student/company/:id",
    component: CompanyDetail,
  },
  {
    path: "/admin/drive/:id",
    component: AdminDriveDetails,
  },
  {
    path: "/admin/application/:id",
    component: AdminApplicationDetails,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// helper to parse JWT payload
function parseJwt(token) {
  if (!token) return null;
  try {
    const base64Url = token.split(".")[1];
    const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split("")
        .map(function (c) {
          return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
        })
        .join(""),
    );

    return JSON.parse(jsonPayload);
  } catch (e) {
    return null;
  }
}

// Global navigation guard for role-based access
router.beforeEach((to, from, next) => {
  const requiredRoles = to.meta && to.meta.roles;

  if (!requiredRoles) return next();

  const token = localStorage.getItem("token");
  if (!token) {
    // not logged in
    return next({ path: "/login" });
  }

  const payload = parseJwt(token);
  const role = payload && (payload.role || payload?.role);

  if (!role || !requiredRoles.includes(role)) {
    alert("Access denied: insufficient permissions");
    // abort navigation and stay on the current page
    return next(false);
  }

  return next();
});

export default router;
