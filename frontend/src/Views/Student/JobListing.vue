<template>
  <div class="container">

    <h1>Browse Jobs</h1>

    <div class="search-bar">
      <input v-model="search" placeholder="Search by title or skills" />
      <button @click="searchJobs">Search</button>
    </div>

    <table>
      <tr>
        <th>Drive</th>
        <th>Title</th>
        <th>Company</th>
        <th>Skills Required</th>
        <th>Location</th>
        <th>Action</th>
      </tr>

      <tr v-for="job in jobs" :key="job.id">
        <td>{{ job.drive }}</td>
        <td>{{ job.title }}</td>
        <td>{{ job.company_name }}</td>
        <td>{{ job.skills_required }}</td>
        <td>{{ job.location }}</td>

        <td>
          <button @click="viewJob(job.id)">View</button>
          <button @click="applyJob(job.id)">Apply</button>
        </td>
      </tr>

    </table>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "JobListing",

  data() {
    return {
      search: "",
      jobs: []
    };
  },

  methods: {

    async getJobs() {
      const res = await api.get("/student/jobs", {
        params: { q: this.search }
      });

      this.jobs = res.data;
    },

    searchJobs() {
      this.getJobs();
    },

    viewJob(id) {
      this.$router.push(`/student/job/${id}`);
    },

    applyJob(id) {
      api.post(`/student/job/${id}/apply`)
        .then((res) => {
          alert(res.data.message);
        })
        .catch((err) => {
          alert(err.response.data.message);
        });
    }

  },

  mounted() {
    this.getJobs();
  }

};
</script>

<style scoped>

.container{
    width:90%;
    margin:auto;
}

.search-bar{
    margin-bottom:20px;
}

.search-bar input{
    padding:8px;
    width:300px;
    margin-right:10px;
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