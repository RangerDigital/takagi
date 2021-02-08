<template>
  <section class="g-full-page">
    <NavigationBar title="My Polls" />
    <div class="g-component-flex">
      <p class="form-label width-30">Polls created by You,</p>

      <div v-if="!pollData.length">
        <p class="form-label width-30"><img class="g-form-icon" src="../assets/icon-msg.svg" alt="Message Icon" />Nothing here... Create some polls!</p>
        <p class="form-label width-30 text-center">. . .</p>
      </div>

      <div v-for="(item, index) in pollData" :key="index">
        <div @click="$router.push('/polls/' + item._id + '/results')">
          <PollQuestion slim class="poll-item g-clickable" v-bind:pollData="item"></PollQuestion>
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
        serverErrorMsg: "",
      };
    },
    methods: {
      getPollData() {
        this.$http
          .get("/api/polls")
          .then((response) => {
            this.pollData = response.data;
          })
          .catch((error) => {
            this.isSuccess = false;
            this.serverErrorMsg = error.response.data.msg;

            if (error.response.status === 401) {
              localStorage.removeItem("jwt_token");
              this.$http.defaults.headers.common["Authorization"] = "";

              this.$router.push("/");
            }
          });
      },
    },
    created() {
      this.getPollData();
    },
  };
</script>

<style scoped>
  .width-30 {
    width: 30rem;
  }

  .form-label {
    color: #626468;
    text-align: left;
  }

  .vertical-divider {
    height: 2px;
    border-radius: 100px;
    width: 100%;
    background-color: #ebebeb;
  }

  .text-center {
    color: #626468;
    text-align: center;
  }

  .poll-item {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;

    transition: all 1s;
  }

  .poll-item:hover {
    transform: rotateZ(2.5deg);
  }
</style>
