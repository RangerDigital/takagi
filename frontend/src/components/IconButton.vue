<template>
<button class="button button-flex g-clickable" @click="$emit('clickEvent');">
  <slot>CLICK ME</slot>
</button>
</template>

<script>
export default {
  name: 'IconButton',
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

.button-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button img {
  height: 2rem;
  margin: 0.6em;
}
</style>
