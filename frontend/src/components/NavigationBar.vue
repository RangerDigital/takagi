<template>
<section>
  <nav class="nav-mobile flex">
    <div class="nav-logo">
      <h1>{{title}}</h1>
      <div class="nav-divider"></div>
    </div>
    
    <router-link to="/navigation"><img src="../assets/icon-nav.svg" class="nav-icon"></router-link>
  </nav>
  
  <nav class="nav-desktop flex">
    <div class="nav-logo">
      <h1>{{title}}</h1>
      <div class="nav-divider"></div>
    </div>
    
    <div class="nav-desktop-links flex">
    <router-link to="/create" class="nav-link"><p>Create Poll</p></router-link>
    
    <!-- If Not Logged -->
    <template v-if="!isLogged">
      <router-link to="/login" class="nav-link"><p>Sign In</p></router-link>
      <router-link to="/register" class="nav-link"><p>Sign Up</p></router-link>
    </template>
    
    <!-- If Logged -->
    <template v-if="isLogged">
      <router-link to="/polls" class="nav-link"><p>Polls</p></router-link>
      <router-link to="/profile" class="nav-link"><p>Profile</p></router-link>
    </template>
    
    </div>
    
  </nav>
</section>
</template>


<script>
export default {
  name: "NavigationBar",
  data() {
    return {
      isLogged: false,
    };
  },
  props: [
    'title',
  ],
}
</script>


<style scoped>

.flex {
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
  max-width: 800px;
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
  opacity: 60%;
}

@media only screen and (min-width: 600px)  {
  .nav-mobile{
    display: none;
  }
}

@media not screen and (min-width: 600px) {
  .nav-desktop {
    display: none;
  }
}

</style>
