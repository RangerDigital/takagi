<template>
<section class="full-page">
  <NavigationBar title="Navigation" mode='back' />

  <div class="navigation-flex">
    <div>
      <IconButton @clickEvent="$router.push('/create')">
        <p>CREATE POLL</p><img src="../assets/icon-arrow-bar.svg" />
      </IconButton>

      <p class="text-label">Create a new poll.</p>
    </div>

    <!-- If Not Logged -->
    <template v-if="!isLogged">
      <div>
        <IconButton @clickEvent="$router.push('/login')">
          <p>SIGN IN</p><img src="../assets/icon-arrow-bar.svg" />
        </IconButton>

        <p class="text-label">Login to your existing account.</p>
      </div>

      <div>
        <IconButton @clickEvent="$router.push('/register')">
          <p>SIGN UP</p><img src="../assets/icon-arrow-bar.svg" />
        </IconButton>

        <p class="text-label">Create a new account.</p>
      </div>
    </template>

    <!-- If Logged -->
    <template v-if="isLogged">
      <div>
        <IconButton @clickEvent="$router.push('/polls')">
          <p>MY POLLS</p><img src="../assets/icon-arrow-bar.svg" />
        </IconButton>

        <p class="text-label">Manage your existing polls.</p>
      </div>

      <div>
        <IconButton @clickEvent="$router.push('/register')">
          <p>MY PROFILE</p><img src="../assets/icon-arrow-bar.svg" />
        </IconButton>

        <p class="text-label">Manage your account.</p>
      </div>
    </template>
  </div>
  <FooterBar />
</section>
</template>


<script>
import NavigationBar from "../components/NavigationBar.vue";
import FooterBar from "../components/FooterBar.vue";

import IconButton from "../components/IconButton.vue";

export default {
  name: "Navigation",
  components: {
    NavigationBar,
    IconButton,
    FooterBar,
  },
  data() {
    return {
      isLogged: false,
    };
  },
  methods: {
    clickTest: function() {
      console.log("Clicked!");
    }
  },
};
</script>


<style scoped>
.navigation-flex {
  min-height: 80%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-around;
}

.text-label {
  color: #626468;
  text-align: center;
}
</style>
