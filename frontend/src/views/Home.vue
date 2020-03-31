<template>
<section class="g-full-page hero-bg">
  <NavigationBar title="Takagi" />
  <div class="component-flex">
    <div>
      <h1 class="hero-text">TAKAGI</h1>

      <div class="heading-text">
        <h1>Create <span class="text-red">instant</span> and</h1>
        <h1><span class="text-red">anonymous</span> polls</h1>
        <h1>for <span class="text-red">free</span> !</h1>
      </div>
    </div>

    <div>
      <p>No registration, Get started!</p>
      <TextButton @clickEvent="$router.push('/create')">CREATE POLL</TextButton>
    </div>

    <div v-if="!isUserLogged">
      <p>Or, To save your polls</p>
      <OutlineButton @clickEvent="$router.push('/register')">SIGN UP</OutlineButton>
      <p class="text-label">Existing user? <a @click="$router.push('/login')" class="text-link">Sign In</a></p>
    </div>

    <div v-else>
      <p>Welcome back! You are logged in,</p>
      <OutlineButton @clickEvent="logoutUser">LOGOUT</OutlineButton>
      <p class="text-label">If you want to logout!</p>
    </div>

  </div>

  <FooterBar />
</section>
</template>

<script>
import FooterBar from "../components/FooterBar.vue";
import TextButton from "../components/TextButton.vue";
import NavigationBar from "../components/NavigationBar.vue";
import OutlineButton from "../components/OutlineButton.vue";


export default {
  name: "Home",
  components: {
    NavigationBar,
    FooterBar,
    TextButton,
    OutlineButton,
  },
  data() {
    return {
      isUserLogged: false,
    };
  },
  methods: {
    logoutUser() {
      localStorage.removeItem('jwt_token');
      this.$http.defaults.headers.common['Authorization'] = '';
      this.$router.push('/login')
    }
  },
  created() {
    // Check if user is logged.
    if (localStorage.getItem('jwt_token')) {
      this.isUserLogged = true;
    }
  },
};
</script>

<style scoped>
.component-flex {
  min-height: 85%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-around;
}

.hero-text {
  text-align: center;

  font-size: 4.5rem;
  font-weight: 600;
}

.heading-text h1 {
  text-align: center;

  font-size: 2.5rem;
  font-weight: 600;

  letter-spacing: 0.1em;
}

.text-link {
  color: #121213;
}

.text-red {
  color: #FF7171;
}

.text-label {
  color: #626468;
  text-align: center;
}

.hero-bg {
  background-image: url("../assets/bg-takagi.svg");
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}

@media only screen and (min-width: 600px) {
  .hero-text {
    font-size: 6.5rem;
  }

  .heading-text h1 {
    font-size: 3.5rem;
  }
}
</style>
