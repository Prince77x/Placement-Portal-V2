<template>
  <div class="container">

    <h1>My Profile</h1>

    <div class="card">

      <label>Education</label>
      <input v-model="education" />

      <label>Skills</label>
      <input v-model="skills" placeholder="e.g. Python, SQL, React" />

      <label>Resume Link</label>
      <input v-model="resume" placeholder="link to resume" />

      <button @click="saveProfile">Save</button>

    </div>

  </div>
</template>

<script>
import api from "../../services/api.js";

export default {
  name: "StudentProfile",

  data() {
    return {
      education: "",
      skills: "",
      resume: ""
    };
  },

  methods: {

    async getProfile() {
      const res = await api.get("/student/dashboard");

      this.education = res.data.student.education;
      this.skills = res.data.student.skills;
      this.resume = res.data.student.resume;
    },

    saveProfile() {
      api.put("/student/profile", {
        education: this.education,
        skills: this.skills,
        resume: this.resume
      }).then(() => {
        alert("Profile updated");
      });
    }

  },

  mounted() {
    this.getProfile();
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

input{
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