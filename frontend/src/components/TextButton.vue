<template>
<button class="button-style g-clickable" @click="$emit('clickEvent');">
  <p>
    <slot>CLICK ME</slot>
  </p>

</button>
</template>

<script>
export default {
  name: 'TextButton',
}
</script>

<style scoped>
.button-style {
  width: 25rem;

  display: block;
  margin: 0 auto;

  background-color: #121213;

  border: none;
  border-radius: 8px;

  margin-top: 1rem;
  margin-bottom: 1rem;
}

.button-style p {
  font-size: 1.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;

  color: #FFFFFF;
  padding: 0.6em;
}

.button-style:disabled {
  opacity: 0.1;
}
</style>
