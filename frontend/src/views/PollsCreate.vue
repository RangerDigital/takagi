<template>
  <section class="g-full-page">
    <NavigationBar title="Create Poll" />
    <ValidationObserver v-slot="{ invalid }">
      <div class="g-component-flex">
        <div>
          <div class="form-input">
            <ValidationProvider rules="required|max:100" v-slot="v">
              <label>
                <p class="form-label"><img class="g-form-icon" src="../assets/icon-edit.svg" alt="Edit Icon" />Poll Question</p>
                <textarea class="form-input-area" v-model="form.question" placeholder="e.g. More free time?" rows="3" cols="33" data-cy="question-input"></textarea>
              </label>
              <p class="text-error" v-if="v.errors.length"><img class="g-form-icon" src="../assets/icon-alert-red.svg" alt="Alert Icon" /> {{ v.errors[0] }}</p>
            </ValidationProvider>
          </div>

          <div class="form-input">
            <ValidationProvider rules="max:50" v-slot="v">
              <label>
                <p class="form-label"><img class="g-form-icon" src="../assets/icon-tag.svg" alt="Tag Icon" />New Option</p>
                <SingleInput v-model="newOption" placeholder="e.g. Yes, of course!" @onEnter="addOption" data-cy="option-input" />
              </label>
              <p class="text-error" v-if="v.errors.length"><img class="g-form-icon" src="../assets/icon-alert-red.svg" alt="Alert Icon" /> {{ v.errors[0] }}</p>
            </ValidationProvider>

            <TextButton @clickEvent="addOption" :disabled="!newOption[0] || invalid">ADD OPTION</TextButton>
          </div>
        </div>

        <div class="options-list">
          <p v-if="form.options[0]" class="form-label"><img class="g-form-icon" src="../assets/icon-clip.svg" alt="Clip Icon" />Available Options ({{ form.options.length }}/5)</p>
          <p v-else class="form-label"><img class="g-form-icon" src="../assets/icon-msg.svg" alt="Message Icon" />Add more options for your voters.</p>

          <div v-for="(item, index) in form.options" :key="index">
            <div class="options-item g-clickable" @click="deleteOption(index)">
              <p> {{ item }} </p>
              <img class="g-form-icon" src="../assets/icon-x-red.svg" />
            </div>
          </div>
        </div>

        <div>
          <TextButton @clickEvent="createPoll" :disabled="invalid || !form.options[1]">CREATE</TextButton>
          <p class="text-error"> {{ serverErrorMsg }} </p>
          <p v-show="isSuccess" class="text-center">Success! You created a new poll!</p>
        </div>
      </div>
    </ValidationObserver>
  </section>
</template>

<script>
  import TextButton from "../components/TextButton.vue";
  import SingleInput from "../components/SingleInput.vue";
  import NavigationBar from "../components/NavigationBar.vue";

  // Setup Vee-Validate
  import { ValidationProvider, ValidationObserver, extend } from "vee-validate";

  import { required, min, max } from "vee-validate/dist/rules";

  extend("required", {
    ...required,
    message: "This field is required!",
  });

  extend("min", {
    ...min,
    message: "Must have at least {length} characters!",
  });

  extend("max", {
    ...max,
    message: "Must have at most {length} characters!",
  });

  export default {
    name: "PollsCreate",
    components: {
      TextButton,
      SingleInput,
      NavigationBar,
      ValidationProvider,
      ValidationObserver,
    },
    data() {
      return {
        form: {
          question: "",
          options: [],
        },

        newOption: "",

        isSuccess: false,
        serverErrorMsg: "",
      };
    },
    methods: {
      addOption() {
        if (this.form.options.length >= 5) {
          return;
        }

        this.form.options.push(this.newOption);
        this.newOption = "";
      },

      deleteOption(index) {
        this.form.options.splice(index, 1);
      },

      createPoll() {
        if (this.isSuccess) {
          return;
        }

        this.$http
          .post("/api/polls", this.form)
          .then((response) => {
            this.isSuccess = true;

            setTimeout(() => {
              this.$router.replace("/polls/" + response.data._id);
            }, 1000);
          })
          .catch((error) => {
            this.isSuccess = false;
            this.serverErrorMsg = error.response.data.msg;
          });
      },
    },
  };
</script>

<style scoped>
  .g-full-page {
    overflow-x: hidden;
  }

  .form-input-area {
    width: 30rem;

    display: block;
    margin: 0 auto;

    background-color: #ffffff;

    border: 1.5px solid #121213;
    border-radius: 5px;

    margin-top: 0.5rem;
    margin-bottom: 1rem;

    font-family: "Baloo Thambi 2";

    text-align: left;

    font-size: 1.6rem;
    font-weight: 500;
    letter-spacing: 0.1em;

    color: #121213;
    padding: 0.6em;
  }

  .form-input {
    margin-top: 1rem;
    margin-bottom: 1rem;
  }

  .form-label {
    color: #626468;
    text-align: left;
  }

  .options-list {
    min-height: 60%;
  }

  .options-item {
    display: flex;
    justify-content: space-between;
    align-items: center;

    width: 30rem;
    border-radius: 5px;

    border: 1.5px solid #f0f0f0;
    margin: 0 auto;

    background-color: #ffffff;

    margin-top: 1rem;
    margin-bottom: 1rem;

    font-size: 1.6rem;
    font-weight: 500;
    letter-spacing: 0.1em;

    color: #626468;
    padding: 0.6em;
  }

  .options-item p {
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    max-width: 85%;
  }

  .options-item:hover {
    border: 1.5px solid #ff7171;
  }

  .text-center {
    color: #626468;
    text-align: center;
  }

  .text-error {
    color: #ff7171;
  }
</style>
