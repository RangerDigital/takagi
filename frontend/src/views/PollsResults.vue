<template>
<section class="g-full-page">
  <NavigationBar title="Results" />
  <div class="g-component-flex">
    <PollQuestion v-bind:pollData="pollData"></PollQuestion>

    <div class="options-list">
      <p class="form-label">And, that's what people think!</p>
      <div v-for="(item, index) in sortedPolls" :key="index">
        <ProgressBar v-bind:percentage="getPercentage(item.votes)">
          <p> {{ item.name }} </p>
        </ProgressBar>

        <div class="options-list-info">
          <p class="form-label">{{ item.votes }} Votes</p>
          <p class="form-label">{{ getPercentage(item.votes) }} %</p>
        </div>
      </div>
    </div>

    <TextButton disabled>SHARE</TextButton>
  </div>
</section>
</template>

<script>
import TextButton from "../components/TextButton.vue";
import PollQuestion from "../components/PollQuestion.vue";
import NavigationBar from "../components/NavigationBar.vue";
import ProgressBar from "../components/ProgressBar.vue";

export default {
  name: "PollsResults",
  components: {
    TextButton,
    PollQuestion,
    NavigationBar,
    ProgressBar,
  },
  data() {
    return {
      pollData: {
        voters: [],
      },

      pollId: '',
      updateInterval: null,

      isSuccess: false,
      serverErrorMsg: '',
    };
  },
  methods: {
    getPollData() {
      this.$http
        .get('/polls/' + this.pollId)
        .then(response => {
          this.pollData = response.data;
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;
        });
    },

    getPercentage(count) {
      if (!count) {
        return 0
      }

      return (count / this.pollData.voters.length * 100).toFixed(0);
    },

    getGradientString(percentage) {
      return 'linear-gradient(to right, #FFAEAE, #FFAEAE ' + percentage + '%, #FFFFFF ' + percentage + '%, #FFFFFF)';
    }
  },
  computed: {
    sortedPolls() {
      function compare(b, a) {
        if (a.votes < b.votes) {
          return -1;
        }
        if (a.votes > b.votes) {
          return 1;
        }
        return 0;
      }

      var unsorted = this.pollData.options
      if (!unsorted) {
        return [];
      }
      return unsorted.sort(compare);
    }
  },
  created() {
    this.pollId = this.$route.params.pollId;
    this.getPollData();

    this.updateInterval = setInterval(() => {
      this.getPollData();
    }, 5000)
  },
  beforeDestroy() {
    clearInterval(this.updateInterval);
  }
};
</script>

<style scoped>
.form-label {
  color: #626468;
  text-align: left;
}

.options-list-info {
  display: flex;
  justify-content: space-between;
}

.options-item {
  width: 30rem;
  border-radius: 5px;

  border: 1.5px solid #121213;
  margin: 0 auto;

  background: linear-gradient(to right, #FFFFFF, #FFFFFF);

  margin-top: 1rem;
  margin-bottom: 1rem;

  font-size: 1.6rem;
  font-weight: 500;
  letter-spacing: 0.1em;

  text-align: center;

  color: #121213;
  padding: 0.6em;
}

.option-item-selected {
  background-color: #121213;
  color: #FFFFFF;
}
</style>
