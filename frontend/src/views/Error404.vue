<template>
<section class="g-full-page">
  <NavigationBar title="Dimension 404" />
  <div class="component-flex">
    <div>
      <h1 class="hero-text">404-<span class="text-red">Chan</span></h1>

      <div class="heading-text">
        <h1>It's not like,</h1>
        <h1>It's your fault, <span class="text-red">Baka</span>!</h1>
      </div>
    </div>

    <div>
      <TextButton class="anim-button" @clickEvent="$router.push('/')">TAKE ME HOME</TextButton>
      <p>Go back to home page!</p>
    </div>
  </div>

  <FooterBar />
</section>
</template>

<script>
import FooterBar from "../components/FooterBar.vue";
import TextButton from "../components/TextButton.vue";
import NavigationBar from "../components/NavigationBar.vue";


export default {
  name: "Error404",
  components: {
    NavigationBar,
    FooterBar,
    TextButton,
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

  animation: flicker-in-1 2s linear both;
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

@keyframes flicker-in-1 {
  0% {
    opacity: 0;
  }

  10% {
    opacity: 0;
  }

  10.1% {
    opacity: 1;
  }

  10.2% {
    opacity: 0;
  }

  20% {
    opacity: 0;
  }

  20.1% {
    opacity: 1;
  }

  20.6% {
    opacity: 0;
  }

  30% {
    opacity: 0;
  }

  30.1% {
    opacity: 1;
  }

  30.5% {
    opacity: 1;
  }

  30.6% {
    opacity: 0;
  }

  45% {
    opacity: 0;
  }

  45.1% {
    opacity: 1;
  }

  50% {
    opacity: 1;
  }

  55% {
    opacity: 1;
  }

  55.1% {
    opacity: 0;
  }

  57% {
    opacity: 0;
  }

  57.1% {
    opacity: 1;
  }

  60% {
    opacity: 1;
  }

  60.1% {
    opacity: 0;
  }

  65% {
    opacity: 0;
  }

  65.1% {
    opacity: 1;
  }

  75% {
    opacity: 1;
  }

  75.1% {
    opacity: 0;
  }

  77% {
    opacity: 0;
  }

  77.1% {
    opacity: 1;
  }

  85% {
    opacity: 1;
  }

  85.1% {
    opacity: 0;
  }

  86% {
    opacity: 0;
  }

  86.1% {
    opacity: 1;
  }

  100% {
    opacity: 1;
  }
}

@media only screen and (min-width: 600px) {
  .hero-text {
    font-size: 9.5rem;
  }

  .heading-text h1 {
    font-size: 3.5rem;
  }
}
</style>
