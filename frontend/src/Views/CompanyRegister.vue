<template>
  <div class="container">

    <div class="register-box">

      <h2>Company Registration</h2>
      <p class="subtitle">Register your company account</p>

      <div
        v-if="message"
        class="success"
      >
        {{ message }}
      </div>

      <div
        v-if="error"
        class="error"
      >
        {{ error }}
      </div>

      <form @submit.prevent="registerCompany">

        <div class="form-group">
          <label>Company Name</label>

          <input
            type="text"
            v-model="company.name"
            placeholder="Enter company name"
            required
          >
        </div>

        <div class="form-group">
          <label>Email</label>

          <input
            type="email"
            v-model="company.email"
            placeholder="Enter company email"
            required
          >
        </div>

        <div class="form-group">
          <label>Password</label>

          <input
            type="password"
            v-model="company.password"
            placeholder="Enter password"
            required
          >
        </div>

        <div class="form-group">
          <label>Description</label>

          <textarea
            rows="4"
            v-model="company.discription"
            placeholder="Write a short description about your company"
            required
          ></textarea>
        </div>

        <button type="submit">
          Register Company
        </button>

      </form>

    </div>

  </div>
</template>

<script>
import { companyRegister } from "../services/auth";

export default {
  name: "CompanyRegister",

  data() {
    return {
      company: {
        name: "",
        email: "",
        password: "",
        discription: "",
      },

      message: "",
      error: "",
    };
  },

  methods: {
    async registerCompany() {

      this.message = "";
      this.error = "";

      try {

        const response = await companyRegister(this.company);

        this.message = response.data.message;

        this.company = {
          name: "",
          email: "",
          password: "",
          discription: "",
        };

        setTimeout(() => {
          this.$router.push("/login");
        }, 2000);

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
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
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

input,
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  font-size: 14px;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #0d6efd;
}

textarea {
  resize: vertical;
}

button {
  width: 100%;
  padding: 12px;
  background: #0d6efd;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #0b5ed7;
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