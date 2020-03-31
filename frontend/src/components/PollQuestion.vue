<template>
<section class="question-container">
  <p class="form-label">Created by {{ pollData.name }}</p>
  <h1 class="text-hero"> {{pollData.question }} </h1>
  <div class="info-flex">
    <p class="form-label"><img class="form-icon" src="../assets/icon-msg.svg">{{ allVoters }} Votes</p>
    <p class="form-label">{{ createdAt }}</p>
  </div>
</section>
</template>

<script>
export default {
  name: 'PollQuestion',
  props: {
    'pollData': {
      type: Object,
    },
  },
  computed: {
    createdAt() {
      var date = new Date(this.pollData.created_at * 1000);

      return date.toLocaleString('en', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      });
    },
    allVoters() {
      var voters = this.pollData.voters;

      if (!voters) {
        return 0;
      }
      return voters.length;
    }
  }
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
