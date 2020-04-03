<template>
<section class="footer-flex" class="g-clickable">
  <a href="https://github.com/RangerDigital/takagi">
    <p class="text-label">GitHub</p>
  </a>

  <a href="https://bednarski.dev" class="g-clickable">
    <p class="text-label">Jakub Bednarski © 2020</p>
  </a>
</section>
</template>

<style scoped>
.footer-flex {
  max-height: 1%;
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
  margin: 1em;
  text-align: center;

  font-size: 1.2rem;
  transition: all 0.5s;
}

.text-label:hover {
  color: #FF7171;
}
</style>
