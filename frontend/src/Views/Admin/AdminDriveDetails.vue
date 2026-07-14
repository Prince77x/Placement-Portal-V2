<template>
  <div class="container">

    <div class="card" v-if="job.id">

      <h1>{{ job.title }}</h1>
      <p><strong>Drive:</strong> {{ job.drive }}</p>
      <p><strong>Company:</strong> {{ job.company_name }}</p>
      <p><strong>Description:</strong> {{ job.description }}</p>
      <p><strong>Skills Required:</strong> {{ job.skills_required }}</p>
      <p><strong>Experience Required:</strong> {{ job.experience_required }}</p>
      <p><strong>Salary Range:</strong> {{ job.salary_range }}</p>
      <p><strong>Location:</strong> {{ job.location }}</p>
      <p><strong>Status:</strong> {{ job.status }}</p>
      <p><strong>Approved:</strong> {{ job.is_approved ? "Yes" : "No" }}</p>

    </div>

    <div class="card">
      <h2>Applicants</h2>

      <table>
        <tr>
          <th>Student Name</th>
          <th>Status</th>
        </tr>

        <tr v-for="app in applications" :key="app.id">
          <td>{{ app.student_name }}</td>
          <td>{{ app.status }}</td>
        </tr>

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
    margin:auto;
}

.card{
    border:1px solid #ddd;
    padding:20px;
    margin-top:20px;
    margin-bottom:20px;
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

</style>