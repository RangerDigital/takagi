<template>
<div id="app">
  <router-view />
</div>
</template>

<style>
@import './assets/css/reset.css';
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

.full-page {
  height: 100vh;
  width: 100vw;
}

@media only screen and (min-width: 600px) {
  html {
    font-size: 8px;
  }
}

@media only screen and (max-height: 550px) {
  .full-page {
    height: 180vh;
  }
}
</style>
