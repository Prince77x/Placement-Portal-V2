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

      <button @click="applyJob(job.id)">Apply</button>

    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "JobDetail",

  data() {
    return {
      job: {}
    };
  },

  methods: {

    async getJob() {
      const jobId = this.$route.params.id;

      const res = await api.get(`/student/job/${jobId}`);

      this.job = res.data;
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
    this.getJob();
  }

};
</script>

<style scoped>

.container{
    width:70%;
    margin:auto;
}

.card{
    border:1px solid #ddd;
    padding:20px;
    margin-top:20px;
}

button{
    margin-top:15px;
    padding:8px 16px;
    cursor:pointer;
}

</style>