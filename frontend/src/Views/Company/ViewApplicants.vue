<template>
  <div class="container">

    <h1>Applicants for {{ job.title }}</h1>

    <table>
      <tr>
        <th>Name</th>
        <th>Email</th>
        <th>Skills</th>
        <th>Resume</th>
        <th>Status</th>
        <th>Action</th>
      </tr>

      <tr v-for="app in applicants" :key="app.application_id">
        <td>{{ app.student.name }}</td>
        <td>{{ app.student.email }}</td>
        <td>{{ app.student.skills }}</td>
        <td>{{ app.student.resume }}</td>
        <td>{{ app.status }}</td>

        <td>
          <button @click="shortlist(app.application_id)">Shortlist</button>
          <button @click="reject(app.application_id)">Reject</button>
          <button @click="select(app.application_id)">Select</button>
        </td>
      </tr>

    </table>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "ViewApplicants",

  data() {
    return {
      job: {},
      applicants: []
    };
  },

  methods: {

    async getApplicants() {
      const jobId = this.$route.params.id;

      const res = await api.get(`/company/job/${jobId}/applicants`);

      this.job = res.data.job;
      this.applicants = res.data.applicants;
    },

    shortlist(id) {
      api.put(`/company/application/${id}/shortlist`)
        .then(() => this.getApplicants());
    },

    reject(id) {
      api.put(`/company/application/${id}/reject`)
        .then(() => this.getApplicants());
    },

    select(id) {
      api.put(`/company/application/${id}/select`)
        .then(() => this.getApplicants());
    }

  },

  mounted() {
    this.getApplicants();
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
    margin-right:8px;
    padding:6px 12px;
    cursor:pointer;
}

</style>