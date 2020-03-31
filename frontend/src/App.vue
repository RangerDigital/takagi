<template>
<div id="app">
  <transition name="fade" mode="out-in">
    <router-view />
  </transition>
</div>
</template>

<script>
export default {
  created() {
    // Load token from localStorage, validate It.
    var jwt_token = localStorage.getItem('jwt_token');
    if (jwt_token) {
      this.$http.defaults.headers.common['Authorization'] = 'Bearer ' + jwt_token;

      this.$http
        .get('/api/users/me')
        .catch(error => {
          console.log(error)

          localStorage.removeItem('jwt_token');
          this.$http.defaults.headers.common['Authorization'] = '';
        });
    }
  },
}
</script>


<style>
/* Box sizing rules */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Remove default padding */
ul[class],
ol[class] {
  padding: 0;
}

/* Remove default margin */
body,
h1,
h2,
h3,
h4,
p,
ul[class],
ol[class],
li,
figure,
figcaption,
blockquote,
dl,
dd {
  margin: 0;
}

/* Set core body defaults */
body {
  min-height: 100vh;
  scroll-behavior: smooth;
  text-rendering: optimizeSpeed;
  line-height: 1.5;
}

/* Remove list styles on ul, ol elements with a class attribute */
ul[class],
ol[class] {
  list-style: none;
}

/* A elements that don't have a class get default styles */
a:not([class]) {
  text-decoration-skip-ink: auto;
}

/* Make images easier to work with */
img {
  max-width: 100%;
  display: block;
}

/* Natural flow and rhythm in articles by default */
article>*+* {
  margin-top: 1em;
}

/* Inherit fonts for inputs and buttons */
input,
button,
textarea,
select {
  font: inherit;
}

@import url('https://fonts.googleapis.com/css?family=Baloo+Thambi+2&display=swap');

html {
  font-size: 10px;
}

h1 {
  font-size: 2.5rem;
  font-weight: 500;
  font-family: 'Baloo Thambi 2';

  color: #121213;
  letter-spacing: 0.05em;
}

p {
  font-size: 1.6rem;
  font-weight: 500;
  font-family: 'Baloo Thambi 2';

  color: #121213;
  letter-spacing: 0.05em;

  text-align: center;
}


/* Global Helpers */
.full-page {
  height: 100vh;
  width: 100vw;
}

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
}

/* View Transition Animations */
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}

@media only screen and (min-width: 1500px) {
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
