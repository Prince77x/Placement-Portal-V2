<template>
  <div class="container">

    <div class="card">

      <div class="header">

        <h2>{{ company.name }}</h2>

        <button
          class="back-btn"
          @click="goBack"
        >
          ← Back
        </button>

      </div>

      <p class="description">
        {{ company.discription }}
      </p>

    </div>

    <div class="card">

      <h3>Available Drives</h3>

      <table>

        <thead>

          <tr>
            <th>Drive</th>
            <th>Title</th>
            <th>Skills Required</th>
            <th>Action</th>
          </tr>

        </thead>

        <tbody>

          <tr
            v-for="job in jobs"
            :key="job.id"
          >
            <td>{{ job.drive }}</td>
            <td>{{ job.title }}</td>
            <td>{{ job.skills_required }}</td>

            <td>
              <button
                class="view-btn"
                @click="viewJob(job.id)"
              >
                View
              </button>
            </td>
          </tr>

          <tr v-if="jobs.length === 0">
            <td
              colspan="4"
              class="empty"
            >
              No jobs available.
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
    },

    goBack() {
      this.$router.go(-1);
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
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:20px;
    margin-bottom:25px;
    background:white;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.description{
    margin-top:15px;
    color:#555;
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

tr:nth-child(even){
    background:#fafafa;
}

.view-btn{
    padding:6px 14px;
    background:#198754;
    color:white;
    border:none;
    border-radius:4px;
    cursor:pointer;
}

.view-btn:hover{
    background:#157347;
}

.empty{
    text-align:center;
    color:#666;
    padding:20px;
}

</style>