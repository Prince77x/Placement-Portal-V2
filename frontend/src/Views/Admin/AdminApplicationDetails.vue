<template>
  <div class="container">

    <div class="card" v-if="application.id">

      <div class="header">

        <h2>Application #{{ application.id }}</h2>

        <button @click="goBack" class="back-btn">
          ← Back
        </button>

      </div>

      <p class="status">
        <strong>Status:</strong> {{ application.status }}
      </p>

      <hr>

      <h3>Student Details</h3>

      <div class="info">
        <p><strong>Name:</strong> {{ application.student.name }}</p>
        <p><strong>Email:</strong> {{ application.student.email }}</p>
        <p><strong>Skills:</strong> {{ application.student.skills }}</p>
        <p><strong>Resume:</strong> {{ application.student.resume }}</p>
      </div>

      <hr>

      <h3>Job Details</h3>

      <div class="info">
        <p><strong>Drive:</strong> {{ application.job.drive }}</p>
        <p><strong>Title:</strong> {{ application.job.title }}</p>
        <p><strong>Company:</strong> {{ application.job.company_name }}</p>
      </div>

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
    },

    goBack() {
      this.$router.go(-1);
    }

  },

  mounted() {
    this.getApplication();
  }

};
</script>

<style scoped>

.container {
  width: 70%;
  margin: 40px auto;
}

.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 25px;
  background: #fff;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.back-btn {
  padding: 8px 16px;
  border: none;
  background: #0d6efd;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.back-btn:hover {
  background: #0b5ed7;
}

.status {
  margin-top: 20px;
  font-size: 16px;
}

h3 {
  margin-top: 25px;
  color: #333;
}

.info p {
  margin: 10px 0;
  font-size: 15px;
}

hr {
  margin: 20px 0;
  border: none;
  border-top: 1px solid #ddd;
}

</style>