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
      <TextButton class="anim-button" @clickEvent="$router.push('/create')">TAKE ME HOME</TextButton>
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

@media only screen and (min-width: 600px) {
  .hero-text {
    font-size: 6.5rem;
  }

  .heading-text h1 {
    font-size: 3.5rem;
  }
}
</style>
