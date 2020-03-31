<template>
<section class="g-full-page">
  <NavigationBar title="Vote" />
  <div class="g-component-flex">
    <PollQuestion v-bind:pollData="pollData"></PollQuestion>

    <div class="options-list">
      <p class="form-label">So, What is Your answer?</p>
      <div v-for="(item, index) in pollData.options" :key="index">
        <p @click="selectOption(index)" class="options-item g-clickable" v-bind:class="{ 'option-item-selected': form.option_id == index }"> {{ item.name }} </p>
      </div>

      <p class="text-center text-link">
        Results? <router-link v-bind:to="'/polls/' + this.pollId + '/results'">See Them Here</router-link>
      </p>
    </div>

    <div>
      <TextButton @clickEvent="voteInPoll" :disabled="form.option_id == -1">VOTE</TextButton>
      <p class="text-error"> {{ serverErrorMsg }} </p>
      <p v-show="isSuccess" class="text-center">Success! You Voted!</p>
    </div>
  </div>
</section>
</template>

<script>
import TextButton from "../components/TextButton.vue";
import PollQuestion from "../components/PollQuestion.vue";
import NavigationBar from "../components/NavigationBar.vue";

import * as Fingerprint2 from 'fingerprintjs2'

export default {
  name: "PollsVote",
  components: {
    TextButton,
    PollQuestion,
    NavigationBar,
  },
  data() {
    return {
      pollData: {},
      pollId: '',

      form: {
        fingerprint: '',
        option_id: -1,
      },

      isSuccess: false,
      serverErrorMsg: '',
    };
  },
  methods: {
    selectOption(index) {
      this.form.option_id = index;
    },

    voteInPoll() {
      if (this.isSuccess) {
        return;
      }

      this.$http
        .post('/polls/' + this.pollId + '/vote', this.form)
        .then(response => {
          console.log(response);
          this.isSuccess = true;

          setTimeout(() => {
            this.$router.replace('/polls/' + this.pollId + '/results');
          }, 1000)
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;
        });
    },

    getFingerprint() {
      var options = {}

      Fingerprint2.get(options, (components) => {
        var values = components.map((component) => {
          return component.value
        })

        this.form.fingerprint = Fingerprint2.x64hash128(values.join(''), 31)
      })
    }
  },
  created() {
    this.pollId = this.$route.params.pollId;

    this.$http
      .get('/polls/' + this.pollId)
      .then(response => {
        console.log(response);
        this.pollData = response.data;

        console.log(response.data)
      })
      .catch(error => {
        this.isSuccess = false;
        this.serverErrorMsg = error.response.data.msg;
      });

    this.getFingerprint();
  }
};
</script>

<style scoped>
.form-label {
  color: #626468;
  text-align: left;
}

.options-item {
  width: 30rem;
  border-radius: 5px;

  border: 1.5px solid #121213;
  margin: 0 auto;

  background-color: #FFFFFF;


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

.options-item:hover {
  background-color: #121213;
  color: #FFFFFF;
}

.text-error {
  color: #FF7171;
}

.text-center {
  color: #626468;
  text-align: center;
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
