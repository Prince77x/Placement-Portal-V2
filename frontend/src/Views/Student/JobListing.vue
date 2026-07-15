<template>
  <div class="container">

    <div class="card">

      <h2>Browse Jobs</h2>

      <div class="search-bar">

        <input
          v-model="search"
          placeholder="Search by title or skills"
        />

        <button
          class="search-btn"
          @click="searchJobs"
        >
          Search
        </button>

      </div>

      <table>

        <thead>

          <tr>
            <th>Drive</th>
            <th>Title</th>
            <th>Company</th>
            <th>Skills Required</th>
            <th>Location</th>
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
            <td>{{ job.company_name }}</td>
            <td>{{ job.skills_required }}</td>
            <td>{{ job.location }}</td>

            <td>

              <button
                class="view-btn"
                @click="viewJob(job.id)"
              >
                View
              </button>

              <button
                class="apply-btn"
                @click="applyJob(job.id)"
              >
                Apply
              </button>

            </td>

          </tr>

          <tr v-if="jobs.length === 0">
            <td colspan="6" class="empty">
              No jobs found.
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
        params: {
          q: this.search
        }
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
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:20px;
    background:white;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
}

h2{
    margin-bottom:20px;
}

.search-bar{
    display:flex;
    gap:10px;
    margin-bottom:20px;
}

.search-bar input{
    flex:1;
    padding:10px;
    border:1px solid #ccc;
    border-radius:5px;
}

.search-bar input:focus{
    outline:none;
    border-color:#0d6efd;
}

.search-btn{
    padding:10px 18px;
    background:#0d6efd;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}

.search-btn:hover{
    background:#0b5ed7;
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

.view-btn{
    background:#0d6efd;
    color:white;
    border:none;
    padding:6px 12px;
    border-radius:4px;
    margin-right:6px;
    cursor:pointer;
}

.apply-btn{
    background:#198754;
    color:white;
    border:none;
    padding:6px 12px;
    border-radius:4px;
    cursor:pointer;
}

.view-btn:hover{
    background:#0b5ed7;
}

.apply-btn:hover{
    background:#157347;
}

.empty{
    text-align:center;
    color:#666;
    padding:20px;
}

</style>