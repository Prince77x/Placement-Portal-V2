<template>
  <div class="home">

    <div class="hero">
      <h1>Placement Portal</h1>
      <p>Connecting Students with Companies</p>

      <router-link to="/login" class="btn primary">
        Login
      </router-link>
    </div>

    <div class="cards">

      <div class="card">
        <h2>Student</h2>
        <p>Register and apply for placement opportunities.</p>

        <router-link
          to="/student/register"
          class="btn green">
          Student Registration
        </router-link>
      </div>

      <div class="card">
        <h2>Company</h2>
        <p>Register your company and post job openings.</p>

        <router-link
          to="/company/register"
          class="btn orange">
          Company Registration
        </router-link>
      </div>

    </div>

    <div class="features">
      <h2>Why Choose Us?</h2>

      <div class="feature-list">

        <div class="feature">
          <h3>Students</h3>
          <p>Apply to multiple companies.</p>
        </div>

        <div class="feature">
          <h3>Companies</h3>
          <p>Hire talented students.</p>
        </div>

        <div class="feature">
          <h3>Admin</h3>
          <p>Manage the complete placement process.</p>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
.home {
  max-width: 1000px;
  margin: 40px auto;
  padding: 20px;
  font-family: Arial, Helvetica, sans-serif;
}

.hero {
  text-align: center;
  margin-bottom: 50px;
}

.hero h1 {
  font-size: 40px;
  margin-bottom: 10px;
}

.hero p {
  color: #555;
  margin-bottom: 20px;
}

.cards {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 50px;
}

.card {
  width: 320px;
  padding: 25px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}

.card h2 {
  margin-bottom: 15px;
}

.card p {
  color: #666;
  margin-bottom: 20px;
}

.btn {
  display: inline-block;
  padding: 10px 18px;
  text-decoration: none;
  color: white;
  border-radius: 5px;
}

.primary {
  background: #007bff;
}

.green {
  background: #28a745;
}

.orange {
  background: #f39c12;
}

.features {
  text-align: center;
}

.features h2 {
  margin-bottom: 30px;
}

.feature-list {
  display: flex;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
}

.feature {
  flex: 1;
  min-width: 220px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.feature p {
  color: #666;
}
</style>