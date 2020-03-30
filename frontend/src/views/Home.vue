<template>
<section class="full-page">
  <NavigationBar title="Takagi" />
  <div class="home-flex">
    <h1 class="home-text-hero">TAKAGI</h1>

    <div class="home-text">
      <h1>Create <span class="text-red">instant</span> and</h1>
      <h1><span class="text-red">anonymous</span> polls</h1>
      <h1>for <span class="text-red">free</span> !</h1>
    </div>

    <div>
      <p>Get started!</p>
      <TextButton @clickEvent="$router.push('/create')">CREATE POLL</TextButton>
    </div>

    <div>
      <p>Or, To save your polls</p>
      <OutlineButton @clickEvent="$router.push('/create')">SIGN UP</OutlineButton>
      <p class="text-label">Existing user? <a class="text-link">Sign In</a></p>
    </div>

    <FooterBar />
  </div>

</section>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import FooterBar from "../components/FooterBar.vue";

import TextButton from "../components/TextButton.vue";
import OutlineButton from "../components/OutlineButton.vue";

export default {
  name: "Home",
  components: {
    NavigationBar,
    FooterBar,
    TextButton,
    OutlineButton,
  }
};
</script>

<style scoped>
.home-flex {
  min-height: 90%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-between;
}

.home-text-hero {
  text-align: center;

  font-size: 4.5rem;
  font-weight: 600;
}

.home-text h1 {
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
</style>
