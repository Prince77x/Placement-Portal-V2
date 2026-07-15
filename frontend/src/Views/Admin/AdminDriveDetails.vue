<template>
  <div class="container">

    <div class="card" v-if="job.id">

      <div class="header">

        <h2>{{ job.title }}</h2>

        <button @click="goBack" class="back-btn">
          ← Back
        </button>

      </div>

      <hr>

      <p><strong>Drive:</strong> {{ job.drive }}</p>
      <p><strong>Company:</strong> {{ job.company_name }}</p>
      <p><strong>Description:</strong> {{ job.description }}</p>
      <p><strong>Skills Required:</strong> {{ job.skills_required }}</p>
      <p><strong>Experience Required:</strong> {{ job.experience_required }}</p>
      <p><strong>Salary Range:</strong> {{ job.salary_range }}</p>
      <p><strong>Location:</strong> {{ job.location }}</p>
      <p><strong>Status:</strong> {{ job.status }}</p>
      <p>
        <strong>Approved:</strong>
        {{ job.is_approved ? "Yes" : "No" }}
      </p>

    </div>

    <div class="card">

      <h3>Applicants</h3>

      <table>

        <thead>

          <tr>
            <th>Student Name</th>
            <th>Status</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="app in applications"
            :key="app.id"
          >
            <td>{{ app.student_name }}</td>
            <td>{{ app.status }}</td>
          </tr>

          <tr v-if="applications.length === 0">
            <td colspan="2" class="empty">
              No applications found.
            </td>
          </tr>

        </tbody>

      </table>

    </div>

  </div>
</template>

<script>
import api from "../../services/api";

export default {
  name: "AdminDriveDetails",

  data() {
    return {
      job: {},
      applications: []
    };
  },

  methods: {

    async getDrive() {

      const jobId = this.$route.params.id;

      const res = await api.get(`/admin/job/${jobId}`);

      this.job = res.data.job;
      this.applications = res.data.applications;

    },

    goBack() {
      this.$router.go(-1);
    }

  },

  mounted() {
    this.getDrive();
  }

};
</script>

<style scoped>

.container{
    width:80%;
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:20px;
    margin-bottom:25px;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
    background:white;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.back-btn{
    padding:8px 16px;
    background:#0d6efd;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}

.back-btn:hover{
    background:#0b5ed7;
}

h2,
h3{
    margin:0;
}

p{
    margin:10px 0;
}

hr{
    margin:20px 0;
    border:none;
    border-top:1px solid #ddd;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:15px;
}

th{
    background:#f4f4f4;
}

th,
td{
    border:1px solid #ddd;
    padding:12px;
    text-align:left;
}

.empty{
    text-align:center;
    color:#666;
    padding:20px;
}

</style>