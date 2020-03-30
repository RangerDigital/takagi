<template>
<button class="button" @click="$emit('clickEvent');">
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
.button {
  width: 25rem;

  display: block;
  margin: 0 auto;

  background-color: #121213;

  border: none;
  border-radius: 8px;

  margin-top: 1rem;
  margin-bottom: 1rem;
}

.button p {
  font-size: 1.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;

  color: #FFFFFF;
  padding: 0.6em;
}
</style>
