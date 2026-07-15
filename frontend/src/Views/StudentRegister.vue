<template>
  <div class="container">

    <div class="register-box">

      <h2>Student Registration</h2>
      <p class="subtitle">Create your student account</p>

      <div v-if="message" class="success">
        {{ message }}
      </div>

      <div v-if="error" class="error">
        {{ error }}
      </div>

      <form @submit.prevent="registerStudent">

        <div class="form-group">
          <label>Name</label>
          <input
            type="text"
            v-model="student.name"
            placeholder="Enter your name"
            required
          >
        </div>

        <div class="form-group">
          <label>Email</label>
          <input
            type="email"
            v-model="student.email"
            placeholder="Enter your email"
            required
          >
        </div>

        <div class="form-group">
          <label>Password</label>
          <input
            type="password"
            v-model="student.password"
            placeholder="Enter your password"
            required
          >
        </div>

        <div class="form-group">
          <label>Education</label>
          <input
            type="text"
            v-model="student.education"
            placeholder="B.Tech, BCA, MCA..."
            required
          >
        </div>

        <div class="form-group">
          <label>Skills</label>
          <input
            type="text"
            v-model="student.skills"
            placeholder="HTML, CSS, JavaScript..."
          >
        </div>

        <div class="form-group">
          <label>Resume Link</label>
          <input
            type="text"
            v-model="student.resume"
            placeholder="Resume URL"
          >
        </div>

        <button type="submit">
          Register
        </button>

      </form>

    </div>

  </div>
</template>

<script>
import { studentRegister } from "../services/auth";

export default {
  name: "StudentRegister",

  data() {
    return {
      student: {
        name: "",
        email: "",
        password: "",
        education: "",
        skills: "",
        resume: "",
      },

      message: "",
      error: "",
    };
  },

  methods: {
    async registerStudent() {
      this.message = "";
      this.error = "";

      try {
        const response = await studentRegister(this.student);

        this.message = response.data.message;

        this.student = {
          name: "",
          email: "",
          password: "",
          education: "",
          skills: "",
          resume: "",
        };

        setTimeout(() => {
          this.$router.push("/login");
        }, 1500);

      } catch (err) {
        this.error =
          err.response?.data?.message ||
          "Registration Failed";
      }
    },
  },
};
</script>

<style scoped>
.container {
  min-height: 100vh;
  background: #f4f6f9;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px;
}

.register-box {
  width: 450px;
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.12);
}

h2 {
  text-align: center;
  margin-bottom: 5px;
}

.subtitle {
  text-align: center;
  color: #666;
  margin-bottom: 25px;
}

.form-group {
  margin-bottom: 16px;
}

label {
  display: block;
  margin-bottom: 6px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

input:focus {
  outline: none;
  border-color: #198754;
}

button {
  width: 100%;
  padding: 12px;
  background: #198754;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #157347;
}

.success {
  background: #d1e7dd;
  color: #0f5132;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
}

.error {
  background: #f8d7da;
  color: #842029;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
}
</style>