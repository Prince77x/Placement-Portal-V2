<template>
  <div class="container">

    <!-- Header -->
    <div class="header">
      <div>
        <h1>Company Dashboard</h1>
        <p>Welcome {{ company.name }}</p>
      </div>

      <div class="actions">
        <button @click="goToCreateDrive">Create Drive</button>
        <button @click="logout">Logout</button>
      </div>
    </div>

    <!-- Upcoming Drives -->
    <div class="card">
      <h2>Upcoming Drives</h2>

      <table>
        <tr>
          <th>Sr. No</th>
          <th>Drive Name</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="job in openJobs"
          :key="job.id"
        >
          <td>{{ job.id }}</td>
          <td>{{ job.drive }}</td>

          <td>
            <button @click="viewApplicants(job.id)">View Details</button>
            <button @click="markComplete(job.id)">Mark as Complete</button>
          </td>
        </tr>

      </table>
    </div>

    <!-- Closed Drives -->
    <div class="card">
      <h2>Closed Drives</h2>

      <table>
        <tr>
          <th>Sr. No</th>
          <th>Drive Name</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="job in closedJobs"
          :key="job.id"
        >
          <td>{{ job.id }}</td>
          <td>{{ job.drive }}</td>

          <td>
            <button @click="reopenDrive(job.id)">Reopen</button>
          </td>
        </tr>

      </table>
    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "CompanyDashboard",

  data() {
    return {
      company: {},
      jobs: []
    };
  },

  computed: {

    openJobs() {
      return this.jobs.filter(job => job.status !== "Closed");
    },

    closedJobs() {
      return this.jobs.filter(job => job.status === "Closed");
    }

  },

  methods: {

    async getDashboard() {
      const res = await api.get("/company/dashboard");

      this.company = res.data.company;
      this.jobs = res.data.jobs;
    },

    goToCreateDrive() {
      this.$router.push("/company/drive/create");
    },

    viewApplicants(id) {
      this.$router.push(`/company/drive/${id}/applicants`);
    },

    markComplete(id) {
      api.put(`/company/job/${id}/complete`)
        .then(() => this.getDashboard());
    },

    reopenDrive(id) {
      api.put(`/company/job/${id}/reopen`)
        .then(() => this.getDashboard());
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