<template>
<section class="full-page">
  <NavigationBar title="Create Poll" />
  <div class="create-flex">
    <TextButton>CREATE</TextButton>

  </div>
</section>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";

import TextButton from "../components/TextButton.vue";

export default {
  name: "Create",
  components: {
    NavigationBar,
    TextButton,
  }
};
</script>

<style scoped>
.create-flex {
  min-height: 90%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-around;
}
</style>
