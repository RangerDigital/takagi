<template>
<section>
  <NavigationBar title="Takagi" />
  <FooterBar />
</section>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import FooterBar from "../components/FooterBar.vue";

export default {
  name: "Home",
  components: {
    NavigationBar,
    FooterBar,
  }
};
</script>

<style scoped>
</style>
