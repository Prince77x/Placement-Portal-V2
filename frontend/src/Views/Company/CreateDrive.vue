<template>
  <div class="container">

    <h1>Create New Drive</h1>

    <div class="card">

      <label>Drive Code</label>
      <input v-model="drive" placeholder="e.g. TCS01" />

      <label>Job Title</label>
      <input v-model="title" placeholder="e.g. Software Engineer" />

      <label>Description</label>
      <textarea v-model="description"></textarea>

      <label>Skills Required</label>
      <input v-model="skills_required" placeholder="e.g. Python, SQL, React" />

      <label>Experience Required</label>
      <input v-model="experience_required" placeholder="e.g. 0-2 years" />

      <label>Salary Range</label>
      <input v-model="salary_range" placeholder="e.g. 4-6 LPA" />

      <label>Location</label>
      <input v-model="location" placeholder="e.g. Bangalore" />

      <button @click="createDrive">Create Drive</button>

    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "CreateDrive",

  data() {
    return {
      drive: "",
      title: "",
      description: "",
      skills_required: "",
      experience_required: "",
      salary_range: "",
      location: ""
    };
  },

  methods: {

    createDrive() {
      api.post("/company/job", {
        drive: this.drive,
        title: this.title,
        description: this.description,
        skills_required: this.skills_required,
        experience_required: this.experience_required,
        salary_range: this.salary_range,
        location: this.location
      }).then(() => {
        this.$router.push("/company/dashboard");
      });
    }

  }

};
</script>

<style scoped>

.container{
    width:60%;
    margin:auto;
}

.card{
    border:1px solid #ddd;
    padding:20px;
    margin-top:20px;
}

label{
    display:block;
    margin-top:12px;
    font-weight:bold;
}

input, textarea{
    width:100%;
    padding:8px;
    margin-top:5px;
}

button{
    margin-top:20px;
    padding:8px 16px;
    cursor:pointer;
}

</style>