<template>
<section class="footer-flex">
  <a href="https://github.com/RangerDigital/takagi">
    <p class="text-label">GitHub</p>
  </a>

  <a href="https://bednarski.dev">
    <p class="text-label">Jakub Bednarski © 2020</p>
  </a>
</section>
</template>

<style scoped>
.footer-flex {
  width: 100%;

  display: flex;
  align-items: center;
  justify-content: space-around;
}

.footer-flex a {
  text-decoration: none;
}

.text-label {
  color: #626468;
  text-align: center;

  font-size: 1.2rem;
}
</style>
