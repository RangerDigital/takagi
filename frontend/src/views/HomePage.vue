<template>
  <section class="g-full-page hero-bg">
    <NavigationBar title="Takagi" disabled />

    <div class="component-flex">
      <div>
        <h1 class="hero-text">Takagi-<span class="text-red">Chan</span></h1>

        <div class="heading-text">
          <h1>Create <span class="text-red">instant</span> and <span class="text-red">anonymous</span> polls for <span class="text-red">free</span>!</h1>
        </div>
      </div>

      <div>
        <p class="text-label">No sign up required!</p>
        <TextButton class="anim-button" @clickEvent="$router.push('/create')">CREATE POLL</TextButton>
      </div>

      <div v-if="!isUserLogged">
        <p class="text-label">Or, To save your polls</p>
        <OutlineButton @clickEvent="$router.push('/register')">SIGN UP</OutlineButton>
        <p class="text-label">Existing user? <a @click="$router.push('/login')" class="text-link g-clickable undeline">Sign In</a></p>
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
    name: "HomePage",
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
        localStorage.removeItem("jwt_token");
        this.$http.defaults.headers.common["Authorization"] = "";
        this.$router.push("/login");
      },
    },
    mounted() {
      // Check if user is logged.
      if (localStorage.getItem("jwt_token")) {
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
    font-size: 4rem;
    font-weight: 600;

    margin-bottom: 3rem;

    font-family: "Poppins";
  }

  .heading-text h1 {
    text-align: center;

    font-size: 2rem;
    font-weight: 600;

    font-family: "Poppins";
    line-height: 3rem;

    letter-spacing: 0.05em;
  }

  .text-link {
    color: #121213;
    text-decoration: none;
    transition: all 0.5s;
  }

  .text-link:hover {
    color: #ff7171;
  }

  .text-red {
    color: #ff7171;
  }

  .text-label {
    color: #626468;
    text-align: center;
  }

  .undeline {
    text-decoration: underline;
  }

  .hero-bg {
    background-image: url("../assets/bg-takagi.svg");
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
  }

  @media only screen and (min-width: 700px) and (max-width: 1300px) {
    .hero-text {
      font-size: 7rem;
    }

    .heading-text h1 {
      font-size: 2.5rem;
    }
  }

  @media only screen and (min-width: 1300px) {
    .hero-text {
      font-size: 9rem;
    }

    .heading-text h1 {
      font-size: 3rem;
    }
  }
</style>
