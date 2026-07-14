<template>
  <div class="container">

    <div class="card" v-if="application.id">

      <h1>{{ application.job_title }}</h1>
      <p><strong>Drive:</strong> {{ application.drive }}</p>
      <p><strong>Company:</strong> {{ application.company_name }}</p>
      <p><strong>Status:</strong> {{ application.status }}</p>

      <div v-if="application.placement">
        <h3>Placement Info</h3>
        <p><strong>Offer Date:</strong> {{ application.placement.offer_date }}</p>
        <p><strong>Joining Date:</strong> {{ application.placement.joining_date }}</p>
        <p><strong>Package:</strong> {{ application.placement.package }}</p>
      </div>

    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "ApplicationDetail",

  data() {
    return {
      application: {}
    };
  },

  methods: {

    async getApplication() {
      const appId = this.$route.params.id;

      const res = await api.get(`/student/application/${appId}`);

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