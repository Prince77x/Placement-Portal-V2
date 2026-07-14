<template>
  <div class="container">

    <!-- Header -->
    <div class="header">
      <div>
        <h1>Students' Dashboard</h1>
        <p>Welcome {{ student.name }}</p>
      </div>

      <div class="actions">
        <button @click="goToProfile">Profile</button>
        <button @click="goToJobs">Browse Jobs</button>
        <button @click="logout">Logout</button>
      </div>
    </div>

    <!-- Organizations -->
    <div class="card">
      <h2>Organizations</h2>

      <table>
        <tr>
          <th>Sr. No</th>
          <th>Company Name</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="company in companies"
          :key="company.id"
        >
          <td>{{ company.id }}</td>
          <td>{{ company.name }}</td>

          <td>
            <button @click="viewCompany(company.id)">View Details</button>
          </td>
        </tr>

      </table>
    </div>

    <!-- Applied Drives -->
    <div class="card">
      <h2>Applied Drives</h2>

      <table>
        <tr>
          <th>Sr. No</th>
          <th>Drive Name</th>
          <th>Company Name</th>
          <th>Status</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="application in applications"
          :key="application.id"
        >
          <td>{{ application.id }}</td>
          <td>{{ application.drive }}</td>
          <td>{{ application.company_name }}</td>
          <td>{{ application.status }}</td>

          <td>
            <button @click="viewApplication(application.id)">View Details</button>
          </td>
        </tr>

      </table>
    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "StudentDashboard",

  data() {
    return {
      student: {},
      companies: [],
      applications: []
    };
  },

  methods: {

    async getDashboard() {
      const res = await api.get("/student/dashboard");

      this.student = res.data.student;
      this.companies = res.data.companies;
      this.applications = res.data.applications;
    },

    goToProfile() {
      this.$router.push("/student/profile");
    },

    goToJobs() {
      this.$router.push("/student/jobs");
    },

    viewCompany(id) {
      this.$router.push(`/student/company/${id}`);
    },

    viewApplication(id) {
      this.$router.push(`/student/application/${id}`);
    },

    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    }

  },

  mounted() {
    this.getDashboard();
  }

};
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

</style>