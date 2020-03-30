<template>
<section class="full-page">
  <NavigationBar title="Sign Up" />
  <div class="register-flex">

    <div>
      <div class="form-input">
        <p class="text-label"><img src="../assets/icon-tag.svg">Name</p>
        <SingleInput v-model="form.name" placeholder="e.g. John" />
        <p class="text-error">. . .</p>
      </div>

      <div class="form-input">
        <p class="text-label"><img src="../assets/icon-lock.svg">E-Mail</p>
        <SingleInput v-model="form.email" type="email" placeholder="e.g. me@gmail.com" />
        <p class="text-error">. . .</p>
      </div>

      <div class="form-input">
        <p class="text-label"><img src="../assets/icon-mail.svg">Password</p>
        <SingleInput v-model="form.password" type="password" placeholder="e.g. Pretty obvious, right?" />
        <p class="text-error">. . .</p>
      </div>

      <p class="text-center">Existing user? <router-link to="/login">Sign In</router-link>
      </p>

    </div>

    <TextButton>REGISTER</TextButton>

  </div>
</section>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import SingleInput from "../components/SingleInput.vue";
import TextButton from "../components/TextButton.vue";

export default {
  name: "Register",
  components: {
    NavigationBar,
    TextButton,
    SingleInput,
  },
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
      },
    };
  },
};
</script>

<style scoped>
.register-flex {
  min-height: 90%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-around;
}

.form-input {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.text-label {
  color: #626468;
  text-align: left;
}

.text-center {
  color: #626468;
  text-align: center;
}

.text-center a {
  text-decoration: none;
  color: #121213;
}

.text-label img {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}
</style>
