<template>
  <div class="container">

    <h1>{{ company.name }}</h1>
    <p>{{ company.discription }}</p>

    <table>
      <tr>
        <th>Drive</th>
        <th>Title</th>
        <th>Skills Required</th>
        <th>Action</th>
      </tr>

      <tr v-for="job in jobs" :key="job.id">
        <td>{{ job.drive }}</td>
        <td>{{ job.title }}</td>
        <td>{{ job.skills_required }}</td>

        <td>
          <button @click="viewJob(job.id)">View</button>
        </td>
      </tr>

    </table>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "CompanyDetail",

  data() {
    return {
      company: {},
      jobs: []
    };
  },

  methods: {

    async getCompany() {
      const companyId = this.$route.params.id;

      const res = await api.get(`/student/company/${companyId}`);

      this.company = res.data.company;
      this.jobs = res.data.jobs;
    },

    viewJob(id) {
      this.$router.push(`/student/job/${id}`);
    }

  },

  mounted() {
    this.getCompany();
  }

};
</script>

<style scoped>

.container{
    width:90%;
    margin:auto;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th,td{
    border:1px solid #ddd;
    padding:10px;
    text-align:left;
}

button{
    padding:6px 12px;
    cursor:pointer;
}

</style>