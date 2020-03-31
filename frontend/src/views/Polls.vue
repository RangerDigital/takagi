<template>
<section class="g-full-page">
  <NavigationBar title="My Polls" />
  <div class="g-component-flex">
    <p class="form-label">Polls created by You,</p>

    <div v-for="(item, index) in pollData" :key="index">
      <div @click="$router.push('/polls/' + item._id + '/results')">
        <PollQuestion slim class="poll-item" v-bind:pollData="item"></PollQuestion>
        <p class="text-center">. . .</p>
      </div>
    </div>

    <TextButton @clickEvent="$router.push('/create')">CREATE POLL</TextButton>
  </div>
</section>
</template>

<script>
import TextButton from "../components/TextButton.vue";
import PollQuestion from "../components/PollQuestion.vue";
import NavigationBar from "../components/NavigationBar.vue";

export default {
  name: "Polls",
  components: {
    TextButton,
    PollQuestion,
    NavigationBar,
  },
  data() {
    return {
      pollData: {},

      isSuccess: false,
      serverErrorMsg: '',
    };
  },
  methods: {
    getPollData() {
      this.$http
        .get('/polls')
        .then(response => {
          this.pollData = response.data;
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;
        });
    },
  },
  created() {
    this.getPollData();
  },
};
</script>

<style scoped>
.g-full-page {
  overflow-x: hidden;
}

.form-label {
  color: #626468;
  text-align: left;

  width: 30rem;
}

.vertical-divider {
  height: 2px;
  border-radius: 100px;
  width: 100%;
  background-color: #EBEBEB;
}

.text-center {
  color: #626468;
  text-align: center;
}

.poll-item {
  margin-top: 0.25rem;
  margin-bottom: 0.25rem;

  padding: 0.5rem;
  border-radius: 5px;
}

.poll-item:hover {
  background-color: #EBEBEB;

}
</style>
