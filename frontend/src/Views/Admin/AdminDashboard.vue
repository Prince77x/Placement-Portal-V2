<template>
  <div class="container">

    <!-- Header -->
    <div class="header">
      <div>
        <h1>Admin Dashboard</h1>
        <p>Welcome {{ admin.name }}</p>
      </div>

      <div class="actions">
        <input
          type="text"
          v-model="search"
          placeholder="Search Student or Company"
        />

        <button @click="searchData">Search</button>

        <button @click="logout">Logout</button>
      </div>
    </div>

    <!-- Registered Companies -->
    <div class="card">
      <h2>Registered Companies</h2>

      <table>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="company in approvedCompanies"
          :key="company.id"
        >
          <td>{{ company.name }}</td>
          <td>{{ company.description }}</td>

          <td>
            <button
              v-if="company.is_active"
              @click="blacklistCompany(company.id)"
            >
              Blacklist
            </button>

            <button
              v-else
              @click="activateCompany(company.id)"
            >
              Activate
            </button>
          </td>
        </tr>

      </table>
    </div>

    <!-- Registered Students -->
    <div class="card">
      <h2>Registered Students</h2>

      <table>

        <tr>
          <th>Name</th>
          <th>Skills</th>
          <th>Resume</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="student in students"
          :key="student.id"
        >
          <td>{{ student.name }}</td>
          <td>{{ student.skills }}</td>
          <td>{{ student.resume }}</td>

          <td>

            <button
              v-if="student.is_active"
              @click="blacklistStudent(student.id)"
            >
              Blacklist
            </button>

            <button
              v-else
              @click="activateStudent(student.id)"
            >
              Activate
            </button>

          </td>

        </tr>

      </table>
    </div>

    <!-- Pending Companies -->

    <div class="card">

      <h2>Company Applications</h2>

      <table>

        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="company in pendingCompanies"
          :key="company.id"
        >

          <td>{{ company.name }}</td>
          <td>{{ company.description }}</td>

          <td>
            <button @click="approveCompany(company.id)">
              Approve
            </button>
          </td>

        </tr>

      </table>

    </div>

    <!-- Drives -->

    <div class="card">

      <h2>Ongoing Drives</h2>

      <table>

        <tr>
          <th>ID</th>
          <th>Drive</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="job in jobs"
          :key="job.id"
        >

          <td>{{ job.id }}</td>
          <td>{{ job.drive }}</td>

          <td>

            <button @click="viewDrive(job.id)">
              View
            </button>

            <button @click="completeDrive(job.id)">
              Complete
            </button>

          </td>

        </tr>

      </table>

    </div>

    <!-- Student Applications -->

    <div class="card">

      <h2>Student Applications</h2>

      <table>

        <tr>

          <th>ID</th>
          <th>Student</th>
          <th>Company</th>
          <th>Action</th>

        </tr>

        <tr
          v-for="application in applications"
          :key="application.id"
        >

          <td>{{ application.id }}</td>
          <td>{{ application.student.name }}</td>
          <td>{{ application.job.company.name }}</td>

          <td>

            <button @click="viewApplication(application.id)">
              View
            </button>

          </td>

        </tr>

      </table>

    </div>

  </div>
</template>

<script>
import api from "../../services/api.js"; // adjust path to wherever api.js lives

export default {
  name: "AdminDashboard",
  data() {
    return { admin: {}, companies: [], students: [], jobs: [], applications: [], search: "" };
  },
  computed: {
    approvedCompanies() { return this.companies.filter(c => c.is_approved); },
    pendingCompanies() { return this.companies.filter(c => !c.is_approved); }
  },
  methods: {
    async getDashboard() {
      const res = await api.get("/admin/dashboard");
      this.admin = res.data.admin;
      this.companies = res.data.companies;
      this.students = res.data.students;
      this.jobs = res.data.jobs;
      this.applications = res.data.applications;
    },
    searchData() { this.getDashboard(); },
    blacklistCompany(id) { api.put(`/company/${id}/blacklist`).then(() => this.getDashboard()); },
    activateCompany(id) { api.put(`/company/${id}/activate`).then(() => this.getDashboard()); },
    blacklistStudent(id) { api.put(`/student/${id}/blacklist`).then(() => this.getDashboard()); },
    activateStudent(id) { api.put(`/student/${id}/activate`).then(() => this.getDashboard()); },
    approveCompany(id) { api.put(`/company/${id}/approve`).then(() => this.getDashboard()); },
    completeDrive(id) { api.put(`/job/${id}/complete`).then(() => this.getDashboard()); },
    viewDrive(id) { this.$router.push(`/admin/drive/${id}`); },
    viewApplication(id) { this.$router.push(`/admin/application/${id}`); },
    logout() { localStorage.removeItem("token"); this.$router.push("/"); }
  },
  mounted() { this.getDashboard(); }
};
// import axios from "axios";

// export default {
//   name: "AdminDashboard",

//   data() {
//     return {

//       admin: {},

//       companies: [],

//       students: [],

//       jobs: [],

//       applications: [],

//       search: ""

//     };
//   },

//   computed: {

//     approvedCompanies() {
//       return this.companies.filter(c => c.is_approved);
//     },

//     pendingCompanies() {
//       return this.companies.filter(c => !c.is_approved);
//     }

//   },

//   methods: {

//     async getDashboard() {

//       const res = await axios.get("http://127.0.0.1:5000/api/admin/dashboard");

//       this.admin = res.data.admin;
//       this.companies = res.data.companies;
//       this.students = res.data.students;
//       this.jobs = res.data.jobs;
//       this.applications = res.data.applications;

//     },

//     searchData() {
//       this.getDashboard();
//     },

//     blacklistCompany(id) {
//       axios.put(`/api/company/${id}/blacklist`)
//         .then(() => this.getDashboard());
//     },

//     activateCompany(id) {
//       axios.put(`/api/company/${id}/activate`)
//         .then(() => this.getDashboard());
//     },

//     blacklistStudent(id) {
//       axios.put(`/api/student/${id}/blacklist`)
//         .then(() => this.getDashboard());
//     },

//     activateStudent(id) {
//       axios.put(`/api/student/${id}/activate`)
//         .then(() => this.getDashboard());
//     },

//     approveCompany(id) {
//       axios.put(`/api/company/${id}/approve`)
//         .then(() => this.getDashboard());
//     },

//     completeDrive(id) {
//       axios.put(`/api/job/${id}/complete`)
//         .then(() => this.getDashboard());
//     },

//     viewDrive(id) {
//       this.$router.push(`/admin/drive/${id}`);
//     },

//     viewApplication(id) {
//       this.$router.push(`/admin/application/${id}`);
//     },

//     logout() {
//       localStorage.removeItem("token");
//       this.$router.push("/");
//     }

//   },

//   mounted() {
//     this.getDashboard();
//   }

// };
</script>

<style scoped>

.container{
    width:90%;
    margin:auto;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}

.card{
    border:1px solid #ddd;
    padding:20px;
    margin-bottom:25px;
}

table{
    width:100%;
    border-collapse:collapse;
}

th,td{
    border:1px solid #ddd;
    padding:10px;
    text-align:left;
}

button{
    margin-right:8px;
    padding:6px 12px;
    cursor:pointer;
}

input{
    padding:7px;
    margin-right:10px;
}

</style>
