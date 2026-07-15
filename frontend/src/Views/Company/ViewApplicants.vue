<template>
  <div class="container">

    <div class="card">

      <div class="header">

        <h2>Applicants for {{ job.title }}</h2>

        <button
          class="back-btn"
          @click="goBack"
        >
          ← Back
        </button>

      </div>

      <table>

        <thead>

          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Skills</th>
            <th>Resume</th>
            <th>Status</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="app in applicants"
            :key="app.application_id"
          >
            <td>{{ app.student.name }}</td>
            <td>{{ app.student.email }}</td>
            <td>{{ app.student.skills }}</td>
            <td>{{ app.student.resume }}</td>
            <td>{{ app.status }}</td>

            <td>

              <button
                class="shortlist-btn"
                @click="shortlist(app.application_id)"
              >
                Shortlist
              </button>

              <button
                class="reject-btn"
                @click="reject(app.application_id)"
              >
                Reject
              </button>

              <button
                class="select-btn"
                @click="select(app.application_id)"
              >
                Select
              </button>

            </td>

          </tr>

          <tr v-if="applicants.length === 0">
            <td colspan="6" class="empty">
              No applicants found.
            </td>
          </tr>

        </tbody>

      </table>

    </div>

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
    },

    goBack() {
      this.$router.go(-1);
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
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:20px;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
    background:white;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}

table{
    width:100%;
    border-collapse:collapse;
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

tr:nth-child(even){
    background:#fafafa;
}

button{
    padding:6px 12px;
    border:none;
    border-radius:4px;
    cursor:pointer;
    margin-right:6px;
}

.back-btn{
    background:#0d6efd;
    color:white;
}

.shortlist-btn{
    background:#ffc107;
    color:black;
}

.reject-btn{
    background:#dc3545;
    color:white;
}

.select-btn{
    background:#198754;
    color:white;
}

button:hover{
    opacity:0.9;
}

.empty{
    text-align:center;
    color:#666;
    padding:20px;
}

</style>