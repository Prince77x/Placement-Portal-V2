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
        <button @click="exportApplications">Export My Applications</button>
        <button @click="logout">Logout</button>
      </div>
    </div>

    <p v-if="exportStatus">{{ exportStatus }}</p>

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
      applications: [],
      exportStatus: "",
      pollInterval: null,
      pollAttempts: 0
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
    },

    exportApplications() {

      if (this.pollInterval) {
        clearInterval(this.pollInterval);
      }

      this.exportStatus = "Starting export...";
      this.pollAttempts = 0;

      api.post("/student/export").then((res) => {
        const taskId = res.data.task_id;
        this.pollExportStatus(taskId);
      });
    },

    pollExportStatus(taskId) {
      this.exportStatus = "Generating your file, please wait...";

      this.pollInterval = setInterval(() => {

        this.pollAttempts++;

        if (this.pollAttempts > 30) {
          clearInterval(this.pollInterval);
          this.exportStatus = "Taking too long. Is the Celery worker running?";
          return;
        }

        api.get(`/task/${taskId}/status`).then((res) => {

          if (res.data.state === "SUCCESS") {
            clearInterval(this.pollInterval);
            this.exportStatus = "Export ready! Downloading...";

            api.get(`/task/${taskId}/download`, { responseType: "blob" }).then((downloadRes) => {
              const url = window.URL.createObjectURL(new Blob([downloadRes.data]));
              const link = document.createElement("a");
              link.href = url;
              link.setAttribute("download", "export.csv");
              document.body.appendChild(link);
              link.click();
              link.remove();

              this.exportStatus = "Export downloaded!";
            });
          }

          if (res.data.state === "FAILURE") {
            clearInterval(this.pollInterval);
            this.exportStatus = "Export failed: " + res.data.error;
          }

        });
      }, 2000);
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