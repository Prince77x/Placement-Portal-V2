<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <div class="card shadow mt-5">
          <div class="card-header text-center">
            <h3>Login</h3>
          </div>

          <div class="card-body">
            <form @submit.prevent="loginUser">
              <div class="mb-3">
                <label>Email</label>

                <input
                  type="email"
                  class="form-control"
                  v-model="email"
                  required
                />
              </div>

              <div class="mb-3">
                <label>Password</label>

                <input
                  type="password"
                  class="form-control"
                  v-model="password"
                  required
                />
              </div>

              <button class="btn btn-primary w-100">Login</button>
            </form>

            <hr />

            <div class="text-center">
              <router-link to="/student/register">
                Student Registration
              </router-link>

              <br />

              <router-link to="/company/register">
                Company Registration
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { login } from "../services/auth";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },

  methods: {
    async loginUser() {
      try {
        const response = await login({
          email: this.email,
          password: this.password,
        });

        localStorage.setItem("token", response.data.token);

        this.$router.push(response.data.redirect);
      } catch (error) {
        alert(error.response.data.message);
      }
    },
  },
};
</script>
