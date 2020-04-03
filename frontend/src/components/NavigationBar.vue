<template>
<section>
  <nav class="nav-mobile flex">
    <div class="nav-logo">
      <h1 class="g-clickable" @click="$router.push('/')">{{title}}</h1>
      <div class="nav-divider"></div>
    </div>

    <!-- Mode: menu - Hamburger Menu -->
    <router-link to="/navigation" v-if="mode == 'menu'" class="g-clickable"><img src="../assets/icon-nav.svg" class="nav-icon" alt="Navigation Button"></router-link>

    <!-- Mode: back - Go Back Button -->
    <img @click="$router.go(-1)" v-if="mode == 'back'" src="../assets/icon-x.svg" class="nav-icon g-clickable" alt="Navigation Button">

  </nav>

  <nav class="nav-desktop flex">
    <div class="nav-logo">
      <h1 class="g-clickable" @click="$router.push('/')">{{title}}</h1>
      <div class="nav-divider"></div>
    </div>

    <div class="nav-desktop-links flex">
      <router-link to="/create" class="nav-link">
        <p>Create Poll</p>
      </router-link>

      <!-- If Not Logged -->
      <template v-if="!isUserLogged">
        <router-link to="/login" class="nav-link">
          <p>Sign In</p>
        </router-link>
        <router-link to="/register" class="nav-link">
          <p>Sign Up</p>
        </router-link>
      </template>

      <!-- If Logged -->
      <template v-if="isUserLogged">
        <router-link to="/polls" class="nav-link">
          <p>Polls</p>
        </router-link>
        <router-link to="/profile" class="nav-link">
          <p>Profile</p>
        </router-link>
      </template>

    </div>

  </nav>
</section>
</template>


<script>
export default {
  name: 'NavigationBar',
  data() {
    return {
      isUserLogged: false,
    };
  },
  props: {
    'title': {
      type: String,
      default: 'Takagi'
    },
    'mode': {
      type: String,
      default: 'menu'
    },
  },
  created() {
    // Check if user is logged.
    if (localStorage.getItem('jwt_token')) {
      this.isUserLogged = true;
    }
  },
}
</script>


<style scoped>
.flex {
  max-height: 10%;

  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  padding: 2rem;
  padding-left: 3rem;
}

.nav-divider {
  width: 60px;
  height: 2.5px;
  background-color: #FF7171;

  border-radius: 1000px;
}

/* Mobile Only */
.nav-icon {
  height: 3.5rem;
  margin: 2rem;
}

/* Desktop Only */
.nav-desktop {
  max-width: 1000px;
  margin: 0 auto;
}

.nav-link {
  text-decoration: none;
}

.nav-link p {
  font-size: 1.5rem;
  padding-left: 3em;
  padding-right: 3em;

  transition: all 0.5s;
}

.nav-link p:hover {
  color: #FF7171;
}

.router-link-active p {
  color: #FF7171;
  opacity: 0.6;
}

@media only screen and (min-width: 600px) {
  .nav-mobile {
    display: none;
  }
}

@media not screen and (min-width: 600px) {
  .nav-desktop {
    display: none;
  }
}
</style>
