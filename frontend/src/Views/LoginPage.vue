<template>
  <div class="container">

    <div class="login-box">

      <h1>Placement Portal</h1>
      <p class="subtitle">Login to continue</p>

      <form @submit.prevent="loginUser">

        <div class="form-group">

          <label>Email</label>

          <input
            type="email"
            v-model="email"
            placeholder="Enter your email"
            required
          />

        </div>

        <div class="form-group">

          <label>Password</label>

          <input
            type="password"
            v-model="password"
            placeholder="Enter your password"
            required
          />

        </div>

        <button type="submit">
          Login
        </button>

      </form>

      <div class="links">

        <p>
          New Student?
          <router-link to="/student/register">
            Register Here
          </router-link>
        </p>

        <p>
          New Company?
          <router-link to="/company/register">
            Register Here
          </router-link>
        </p>

      </div>

    </div>

  </div>
</template>

<script>
import { login } from "../services/auth";

export default {
  name: "LoginPage",

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
        localStorage.setItem("role", response.data.role);

        this.$router.push(response.data.redirect);

      } catch (error) {

        alert(error.response.data.message);

      }
    },
  },
};
</script>

<style scoped>

*{
    box-sizing:border-box;
}

.container{
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    background:#f2f5f9;
}

.login-box{
    width:380px;
    background:white;
    padding:35px;
    border-radius:10px;
    box-shadow:0 6px 20px rgba(0,0,0,0.1);
}

h1{
    text-align:center;
    margin-bottom:8px;
    color:#0d6efd;
}

.subtitle{
    text-align:center;
    color:#666;
    margin-bottom:25px;
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
    padding:11px;
    border:1px solid #ccc;
    border-radius:6px;
    font-size:15px;
}

input:focus{
    outline:none;
    border-color:#0d6efd;
}

button{
    width:100%;
    padding:12px;
    margin-top:10px;
    background:#0d6efd;
    color:white;
    border:none;
    border-radius:6px;
    font-size:16px;
    cursor:pointer;
}

button:hover{
    background:#0b5ed7;
}

.links{
    margin-top:25px;
    text-align:center;
    border-top:1px solid #ddd;
    padding-top:20px;
}

.links p{
    margin:10px 0;
}

.links a{
    text-decoration:none;
    color:#0d6efd;
    font-weight:bold;
}

.links a:hover{
    text-decoration:underline;
}

</style>