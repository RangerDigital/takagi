<template>
<section class="g-full-page">
  <NavigationBar title="Navigation" mode="back" />

  <div class="component-flex">
    <div>
      <IconButton @clickEvent="$router.push('/create')">
        <p>CREATE POLL</p><img src="../assets/icon-arrow-bar.svg" />
      </IconButton>

      <p class="text-label">Create a new poll.</p>
    </div>

    <!-- If Not Logged -->
    <template v-if="!isUserLogged">
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
    <template v-if="isUserLogged">
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
import FooterBar from "../components/FooterBar.vue";
import NavigationBar from "../components/NavigationBar.vue";

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
      isUserLogged: false,
    };
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

.text-label {
  color: #626468;
  text-align: center;
}
</style>
