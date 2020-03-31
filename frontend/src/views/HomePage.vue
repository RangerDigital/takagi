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

    <!-- <div>
      <p>No sign up required!</p>
      <TextButton class="anim-button" @clickEvent="$router.push('/create')">CREATE POLL</TextButton>
    </div> -->

    <div v-if="!isUserLogged">
      <p>Or, To save your polls</p>
      <OutlineButton @clickEvent="$router.push('/register')">SIGN UP</OutlineButton>
      <p class="text-label">Existing user? <a @click="$router.push('/login')" class="text-link g-clickable">Sign In</a></p>
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
// import TextButton from "../components/TextButton.vue";
import NavigationBar from "../components/NavigationBar.vue";
import OutlineButton from "../components/OutlineButton.vue";


export default {
  name: "HomePage",
  components: {
    NavigationBar,
    FooterBar,
    // TextButton,
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
  mounted() {
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

  animation: opacity-in 1s ease-out;
}

.hero-text {
  text-align: center;
  font-size: 4.5rem;
  font-weight: 600;

  animation: text-focus-in 1s cubic-bezier(0.550, 0.085, 0.680, 0.530);
}

.heading-text h1 {
  text-align: center;

  font-size: 2.5rem;
  font-weight: 600;

  letter-spacing: 0.1em;
}

.text-link {
  color: #121213;
  text-decoration: none;
  transition: all 0.5s;
}

.text-link:hover {
  color: #FF7171;
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

.anim-button {
  animation: pulsate-bck 2s ease-in-out infinite both;
}

@keyframes pulsate-bck {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(0.97);
  }

  100% {
    transform: scale(1);
  }
}

@keyframes text-focus-in {
  0% {
    filter: blur(12px);
    opacity: 0;
  }

  100% {
    filter: blur(0px);
    opacity: 1;
  }
}

@keyframes opacity-in {
  0% {
    opacity: 0%;
  }

  100% {
    opacity: 100%;
  }
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
