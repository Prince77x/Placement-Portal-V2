<template>
  <div class="container">

    <div
      class="card"
      v-if="job.id"
    >

      <div class="header">

        <h2>{{ job.title }}</h2>

        <button
          class="back-btn"
          @click="goBack"
        >
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

      <button
        class="apply-btn"
        @click="applyJob(job.id)"
      >
        Apply Now
      </button>

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

    },

    goBack() {
      this.$router.go(-1);
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
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:25px;
    background:white;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

hr{
    margin:20px 0;
    border:none;
    border-top:1px solid #ddd;
}

p{
    margin:10px 0;
}

.back-btn{
    padding:8px 16px;
    border:none;
    border-radius:5px;
    background:#0d6efd;
    color:white;
    cursor:pointer;
}

.back-btn:hover{
    background:#0b5ed7;
}

.apply-btn{
    margin-top:20px;
    padding:10px 18px;
    border:none;
    border-radius:5px;
    background:#198754;
    color:white;
    cursor:pointer;
    font-size:15px;
}

.apply-btn:hover{
    background:#157347;
}

</style>