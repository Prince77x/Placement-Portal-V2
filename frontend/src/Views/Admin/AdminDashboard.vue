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
          placeholder="student, organization"
        />

        <button @click="searchData">Search</button>

        <button @click="logout">Logout</button>
      </div>
    </div>

    <!-- Stats -->
    <div class="card stats">
      <div>
        <h3>{{ stats.total_students }}</h3>
        <p>Students</p>
      </div>
      <div>
        <h3>{{ stats.total_companies }}</h3>
        <p>Companies</p>
      </div>
      <div>
        <h3>{{ stats.total_jobs }}</h3>
        <p>Job Postings</p>
      </div>
      <div>
        <h3>{{ stats.total_applications }}</h3>
        <p>Applications</p>
      </div>
    </div>

    <!-- Registered Companies -->
    <div class="card">
      <h2>Registered Companies</h2>

      <table>
        <tr>
          <th>Company Name</th>
          <th>Description</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="company in approvedCompanies"
          :key="company.id"
        >
          <td>{{ company.name }}</td>
          <td>{{ company.discription }}</td>

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

            <button @click="removeCompany(company.id)">Remove</button>
          </td>
        </tr>

      </table>
    </div>

    <!-- Registered Students -->
    <div class="card">
      <h2>Registered Students</h2>

      <table>

        <tr>
          <th>Student Name</th>
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

            <button @click="removeStudent(student.id)">Remove</button>

          </td>

        </tr>

      </table>
    </div>

    <!-- Company Applications (pending approval) -->
    <div class="card">

      <h2>Company Applications</h2>

      <table>

        <tr>
          <th>Company Name</th>
          <th>Description</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="company in pendingCompanies"
          :key="company.id"
        >

          <td>{{ company.name }}</td>
          <td>{{ company.discription }}</td>

          <td>
            <button @click="approveCompany(company.id)">
              Approve
            </button>
          </td>

        </tr>

      </table>

    </div>

    <!-- Pending Job Approvals -->
    <div class="card">

      <h2>Pending Job Approvals</h2>

      <table>

        <tr>
          <th>ID</th>
          <th>Drive</th>
          <th>Company</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="job in pendingJobs"
          :key="job.id"
        >

          <td>{{ job.id }}</td>
          <td>{{ job.drive }}</td>
          <td>{{ job.company_name }}</td>

          <td>
            <button @click="approveJob(job.id)">Approve</button>
            <button @click="removeJob(job.id)">Remove</button>
          </td>

        </tr>

      </table>

    </div>

    <!-- Ongoing Drives -->
    <div class="card">

      <h2>Ongoing Drives</h2>

      <table>

        <tr>
          <th>Sr. No</th>
          <th>Drive Name</th>
          <th>Action</th>
        </tr>

        <tr
          v-for="job in ongoingJobs"
          :key="job.id"
        >

          <td>{{ job.id }}</td>
          <td>{{ job.drive }}</td>

          <td>

            <button @click="viewDrive(job.id)">
              View Details
            </button>

            <button @click="completeDrive(job.id)">
              Mark as Complete
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

          <th>Sr. No</th>
          <th>Student Name</th>
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
              View Details
            </button>

          </td>

        </tr>

      </table>

    </div>

  </div>
</template>

<script>
import api from "../../services/api";

export default {
  name: "AdminDashboard",

  data() {
    return {

      admin: {},

      companies: [],

      students: [],

      jobs: [],

      applications: [],

      stats: {},

      search: ""

    };
  },

  computed: {

    approvedCompanies() {
      return this.companies.filter(c => c.is_approved);
    },

    pendingCompanies() {
      return this.companies.filter(c => !c.is_approved);
    },

    pendingJobs() {
      return this.jobs.filter(j => !j.is_approved);
    },

    ongoingJobs() {
      return this.jobs.filter(j => j.is_approved && j.status !== "Closed");
    }

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

    async getStats() {
      const res = await api.get("/admin/stats");
      this.stats = res.data;
    },

    async searchData() {

      if (!this.search) {
        this.getDashboard();
        return;
      }

      const res = await api.get("/admin/search", {
        params: { q: this.search }
      });

      this.companies = res.data.companies.map(c => ({
        ...c,
        is_approved: true,
        is_active: true
      }));

      this.students = res.data.students.map(s => ({
        ...s,
        is_active: true
      }));

    },

    blacklistCompany(id) {
      api.put(`/company/${id}/blacklist`)
        .then(() => this.getDashboard());
    },

    activateCompany(id) {
      api.put(`/company/${id}/activate`)
        .then(() => this.getDashboard());
    },

    removeCompany(id) {
      api.delete(`/company/${id}/remove`)
        .then(() => this.getDashboard())
        .catch(err => alert(err.response.data.message));
    },

    blacklistStudent(id) {
      api.put(`/student/${id}/blacklist`)
        .then(() => this.getDashboard());
    },

    activateStudent(id) {
      api.put(`/student/${id}/activate`)
        .then(() => this.getDashboard());
    },

    removeStudent(id) {
      api.delete(`/student/${id}/remove`)
        .then(() => this.getDashboard())
        .catch(err => alert(err.response.data.message));
    },

    approveCompany(id) {
      api.put(`/company/${id}/approve`)
        .then(() => this.getDashboard());
    },

    approveJob(id) {
      api.put(`/job/${id}/approve`)
        .then(() => this.getDashboard());
    },

    removeJob(id) {
      api.delete(`/job/${id}/remove`)
        .then(() => this.getDashboard())
        .catch(err => alert(err.response.data.message));
    },

    completeDrive(id) {
      api.put(`/job/${id}/complete`)
        .then(() => this.getDashboard());
    },

    viewDrive(id) {
      this.$router.push(`/admin/drive/${id}`);
    },

    viewApplication(id) {
      this.$router.push(`/admin/application/${id}`);
    },

    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    }

  },

  mounted() {
    this.getDashboard();
    this.getStats();
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

.stats{
    display:flex;
    justify-content:space-around;
    text-align:center;
}

.stats h3{
    font-size:28px;
    margin:0;
}

.stats p{
    margin:5px 0 0;
    color:#666;
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