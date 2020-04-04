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

    <div v-if="isOwnedByUser" class="button-list">
      <TextButton @clickEvent="deletePoll" class="button-delete"><img class="form-icon" src="../assets/icon-x-white.svg"></TextButton>
      <TextButton @clickEvent="sharePoll" class="button-small">{{ buttonMsg }}</TextButton>
    </div>
    <TextButton @clickEvent="sharePoll" v-else>{{ buttonMsg }}</TextButton>

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
      userId: '',

      updateInterval: null,

      buttonMsg: 'SHARE',

      isSuccess: false,
      serverErrorMsg: '',
    };
  },
  methods: {
    getPollData() {
      this.$http
        .get('/api/polls/' + this.pollId)
        .then(response => {
          this.pollData = response.data;
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;

          if (error.response.status == 404) {
            this.$router.push('/404');
          }
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
    },

    deletePoll() {
      this.$http
        .delete('/api/polls/' + this.pollId)
        .then(() => {
          this.$router.push('/polls');
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;
        });
    },

    sharePoll() {
      if (navigator.share) {
        navigator.share({
          title: 'Just Takagi',
          url: 'https://takagi.bednarski.dev/polls/' + this.pollId,
          text: 'Hello! Take this poll for me, please?'
        });

      } else {
        navigator.clipboard.writeText('https://takagi.bednarski.dev/polls/' + this.pollId)
        this.buttonMsg = 'LINK COPIED'
      }
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
    },

    isOwnedByUser() {
      if (this.pollData._user_id == this.userId) {
        return true;
      }
      return false;
    }
  },
  created() {
    this.pollId = this.$route.params.pollId;
    this.getPollData();

    this.$http
      .get('/api/users/me')
      .then(response => {
        this.userId = response.data._id;
      })
      .catch(error => {
        console.log(error)
      });

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
.g-full-page {
  overflow-x: hidden;
}

.form-label {
  color: #626468;
  text-align: left;
}

.options-list {
  min-height: 60%;
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

.button-list {
  width: 30rem;
  display: flex;
  justify-content: space-between;
}

.button-delete {
  background-color: #FF7171;
  width: 5rem;
}

.button-small {
  width: 20rem;
}

.form-icon {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}
</style>
