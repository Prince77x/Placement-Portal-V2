<template>
  <div class="container">

    <div class="card" v-if="application.id">

      <h1>Application #{{ application.id }}</h1>
      <p><strong>Status:</strong> {{ application.status }}</p>

      <h3>Student</h3>
      <p><strong>Name:</strong> {{ application.student.name }}</p>
      <p><strong>Email:</strong> {{ application.student.email }}</p>
      <p><strong>Skills:</strong> {{ application.student.skills }}</p>
      <p><strong>Resume:</strong> {{ application.student.resume }}</p>

      <h3>Job</h3>
      <p><strong>Drive:</strong> {{ application.job.drive }}</p>
      <p><strong>Title:</strong> {{ application.job.title }}</p>
      <p><strong>Company:</strong> {{ application.job.company_name }}</p>

    </div>

  </div>
</template>

<script>
import api from "../../services/api";

export default {
  name: "AdminApplicationDetails",

  data() {
    return {
      application: {}
    };
  },

  methods: {

    async getApplication() {
      const appId = this.$route.params.id;

      const res = await api.get(`/admin/application/${appId}`);

      this.application = res.data;
    }

  },

  mounted() {
    this.getApplication();
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

</style>