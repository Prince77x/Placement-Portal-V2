<template>
  <div class="container">

    <div
      class="card"
      v-if="application.id"
    >

      <div class="header">

        <h2>{{ application.job_title }}</h2>

        <button
          class="back-btn"
          @click="goBack"
        >
          ← Back
        </button>

      </div>

      <hr>

      <p><strong>Drive:</strong> {{ application.drive }}</p>
      <p><strong>Company:</strong> {{ application.company_name }}</p>
      <p><strong>Status:</strong> {{ application.status }}</p>

      <div
        v-if="application.placement"
        class="placement"
      >

        <h3>Placement Information</h3>

        <p>
          <strong>Offer Date:</strong>
          {{ application.placement.offer_date }}
        </p>

        <p>
          <strong>Joining Date:</strong>
          {{ application.placement.joining_date }}
        </p>

        <p>
          <strong>Package:</strong>
          {{ application.placement.package }}
        </p>

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

hr{
    margin:20px 0;
    border:none;
    border-top:1px solid #ddd;
}

p{
    margin:10px 0;
}

.placement{
    margin-top:25px;
    padding:15px;
    border:1px solid #ddd;
    border-radius:6px;
    background:#f8f9fa;
}

.placement h3{
    margin-top:0;
    margin-bottom:15px;
}

</style>