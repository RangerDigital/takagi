<template>
<button class="button" @click="$emit('clickEvent');">
  <p>
    <slot>CLICK ME</slot>
  </p>

</button>
</template>

<script>
export default {
  name: 'OutlineButton',
}
</script>

<style scoped>
.button {
  width: 25rem;

  display: block;
  margin: 0 auto;

  background-color: #FFFFFF;

  border: 2.5px solid #121213;
  border-radius: 8px;

  margin-top: 1rem;
  margin-bottom: 1rem;
}

.button p {
  font-size: 1.7rem;
  font-weight: 600;
  letter-spacing: 0.1em;

  color: #121213;
  padding: 0.6em;
}

.button:disabled {
  opacity: 10%;
}
</style>
