<template>
  <div class="container mt-5">

    <div class="row justify-content-center">

      <div class="col-md-6">

        <div class="card shadow">

          <div class="card-header text-center">
            <h3>Company Registration</h3>
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

            <form @submit.prevent="registerCompany">

              <div class="mb-3">
                <label>Company Name</label>

                <input
                  type="text"
                  class="form-control"
                  v-model="company.name"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Email</label>

                <input
                  type="email"
                  class="form-control"
                  v-model="company.email"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Password</label>

                <input
                  type="password"
                  class="form-control"
                  v-model="company.password"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Description</label>

                <textarea
                  class="form-control"
                  rows="4"
                  v-model="company.discription"
                  required
                ></textarea>
              </div>

              <button
                class="btn btn-primary w-100"
                type="submit"
              >
                Register Company
              </button>

            </form>

          </div>

        </div>

      </div>

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