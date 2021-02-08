<template>
  <div id="app">
    <!-- <transition name="fade" mode="out-in"> -->
    <router-view />
    <!-- </transition> -->
  </div>
</template>

<script>
  export default {
    mounted() {
      // Load token from localStorage, validate It.
      var jwt_token = localStorage.getItem("jwt_token");
      if (jwt_token) {
        this.$http.defaults.headers.common["Authorization"] = "Bearer " + jwt_token;

        this.$http.get("/api/users/me").catch((error) => {
          console.log(error);

          localStorage.removeItem("jwt_token");
          this.$http.defaults.headers.common["Authorization"] = "";
        });
      }
    },
  };
</script>

<style>
  @import "./assets/css/reset.css";
  @import url("https://fonts.googleapis.com/css?family=Baloo+Thambi+2&display=swap");
  @import url("https://fonts.googleapis.com/css?family=Poppins&display=swap");

  html {
    font-size: 10px;
    overflow-y: hidden;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: 500;
    font-family: "Baloo Thambi 2";

    color: #121213;
    letter-spacing: 0.04em;
  }

  p {
    font-size: 1.5rem;
    font-weight: 500;
    font-family: "Baloo Thambi 2";

    color: #121213;
    letter-spacing: 0.04em;

    text-align: center;
  }

  /* Global Helpers */
  .g-full-page {
    height: 100vh;
    width: 100vw;
  }

  .g-component-flex {
    min-height: 87%;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: space-around;
  }

  .g-clickable {
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  .g-form-icon {
    display: inline;

    height: 2rem;
    vertical-align: middle;

    margin-right: 0.5rem;
  }

  /* View Transition Animations */
  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.07s;
    transition-property: opacity;
    transition-timing-function: ease-in-out;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0;
  }

  @media only screen and (min-width: 1500px) {
    html {
      font-size: 11px;
    }
  }

  @media only screen and (min-width: 2000px) {
    html {
      font-size: 13px;
    }
  }

  @media only screen and (max-height: 500px) {
    .g-full-page {
      height: 200vh;
    }
  }
</style>
