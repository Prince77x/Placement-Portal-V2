<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">

        <div class="card shadow">

          <div class="card-header text-center">
            <h3>Student Registration</h3>
          </div>

          <div class="card-body">

            <div
              v-if="message"
              class="alert alert-success"
            >
              {{ message }}
            </div>

            <div
              v-if="error"
              class="alert alert-danger"
            >
              {{ error }}
            </div>

            <form @submit.prevent="registerStudent">

              <div class="mb-3">
                <label>Name</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="student.name"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Email</label>
                <input
                  type="email"
                  class="form-control"
                  v-model="student.email"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Password</label>
                <input
                  type="password"
                  class="form-control"
                  v-model="student.password"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Education</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="student.education"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Skills</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="student.skills"
                />
              </div>

              <div class="mb-3">
                <label>Resume Link</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="student.resume"
                />
              </div>

              <button
                class="btn btn-success w-100"
                type="submit"
              >
                Register
              </button>

            </form>

          </div>

        </div>

      </div>
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
      this.message = ""; //this will reset message again 
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