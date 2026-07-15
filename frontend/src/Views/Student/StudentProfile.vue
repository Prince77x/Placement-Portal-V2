<template>
  <div class="container">

    <div class="card">

      <div class="header">

        <h2>My Profile</h2>

        <button
          class="back-btn"
          @click="goBack"
        >
          ← Back
        </button>

      </div>

      <div class="form-group">

        <label>Education</label>

        <input
          v-model="education"
          placeholder="Enter your education"
        />

      </div>

      <div class="form-group">

        <label>Skills</label>

        <input
          v-model="skills"
          placeholder="e.g. Python, SQL, React"
        />

      </div>

      <div class="form-group">

        <label>Resume Link</label>

        <input
          v-model="resume"
          placeholder="Paste your resume link"
        />

      </div>

      <button
        class="save-btn"
        @click="saveProfile"
      >
        Save Profile
      </button>

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

    },

    goBack() {
      this.$router.go(-1);
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
    margin:40px auto;
}

.card{
    border:1px solid #ddd;
    border-radius:8px;
    padding:25px;
    box-shadow:0 3px 10px rgba(0,0,0,0.08);
    background:white;
}

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:20px;
}

.form-group{
    margin-bottom:18px;
}

label{
    display:block;
    margin-bottom:6px;
    font-weight:bold;
}

input{
    width:100%;
    padding:10px;
    border:1px solid #ccc;
    border-radius:5px;
    box-sizing:border-box;
}

input:focus{
    outline:none;
    border-color:#198754;
}

.save-btn{
    margin-top:10px;
    padding:10px 18px;
    border:none;
    border-radius:5px;
    background:#198754;
    color:white;
    cursor:pointer;
}

.save-btn:hover{
    background:#157347;
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

</style>