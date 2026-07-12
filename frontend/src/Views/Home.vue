<template>
  <div class="container mt-5">

    <div class="text-center">

      <h1 class="display-4 fw-bold">
        Placement Portal
      </h1>

      <p class="lead">
        Connecting Students with Companies
      </p>

      <router-link
        to="/login"
        class="btn btn-primary btn-lg m-2">

        Login

      </router-link>

    </div>

    <hr class="my-5">

    <div class="row">

      <div class="col-md-6 text-center">

        <h3>Student</h3>

        <p>
          Register and apply for placement opportunities.
        </p>

        <router-link
          to="/student/register"
          class="btn btn-success">

          Student Registration

        </router-link>

      </div>

      <div class="col-md-6 text-center">

        <h3>Company</h3>

        <p>
          Register your company and post job openings.
        </p>

        <router-link
          to="/company/register"
          class="btn btn-warning">

          Company Registration

        </router-link>

      </div>

    </div>

    <hr class="my-5">

    <div class="text-center">

      <h2>Why Choose Us?</h2>

      <div class="row mt-4">

        <div class="col-md-4">

          <h5>Students</h5>

          <p>Apply to multiple companies.</p>

        </div>

        <div class="col-md-4">

          <h5>Companies</h5>

          <p>Hire talented students.</p>

        </div>

        <div class="col-md-4">

          <h5>Admin</h5>

          <p>Manage the complete placement process.</p>

        </div>

      </div>

    </div>

  </div>
</template>

<script>
export default {
    name:"HomePage"
}
</script>