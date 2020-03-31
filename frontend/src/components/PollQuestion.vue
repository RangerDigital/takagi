<template>
<section class="question-container">
  <p class="form-label">Created by {{ pollData.name }}</p>
  <h1 class="text-hero"> {{pollData.question }} </h1>
  <div class="info-flex">
    <p class="form-label"><img class="form-icon" src="../assets/icon-msg.svg">12 Votes</p>
    <p class="form-label">23 March 2020</p>
  </div>
</section>
</template>

<script>
export default {
  name: 'PollQuestion',
  props: {
    'pollData': {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.question-container {
  width: 30rem;

  margin: 0 auto;
}

.text-center {
  color: #626468;
  text-align: center;
}

.form-label {
  color: #626468;
  text-align: left;
}

.text-error {
  color: #FF7171;
}

.info-flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text-hero {
  margin-top: 0.5em;
  margin-bottom: 0.5em;
}

.text-link a {
  text-decoration: none;
  color: #121213;
}

.form-icon {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}
</style>
