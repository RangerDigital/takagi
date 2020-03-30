<template>
<section class="full-page">
  <NavigationBar title="Sign Up" />
  <div class="register-flex">

    <ValidationObserver v-slot="{ invalid }">
      <div>
        <div class="form-input">
          <p class="text-label"><img src="../assets/icon-tag.svg">Name</p>
          <ValidationProvider rules="required|min:3|max:15" v-slot="v">
            <SingleInput v-model.lazy="form.name" placeholder="e.g. John" />
            <p class="text-error" v-if="v.errors.length"><img class="icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
            <p class="text-center" v-else>. . .</p>
          </ValidationProvider>
        </div>

        <div class="form-input">
          <p class="text-label"><img src="../assets/icon-lock.svg">E-Mail</p>
          <ValidationProvider rules="required|email" v-slot="v">
            <SingleInput v-model.lazy="form.email" type="email" placeholder="e.g. me@gmail.com" />
            <p class="text-error" v-if="v.errors.length"><img class="icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
            <p class="text-center" v-else>. . .</p>
          </ValidationProvider>
        </div>

        <div class="form-input">
          <p class="text-label"><img src="../assets/icon-mail.svg">Password</p>
          <ValidationProvider rules="required|min:8" v-slot="v">
            <SingleInput v-model.lazy="form.password" type="password" placeholder="e.g. Pretty obvious, right?" />
            <p class="text-error" v-if="v.errors.length"><img class="icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
            <p class="text-center" v-else>. . .</p>
          </ValidationProvider>
        </div>


        <p class="text-center">Existing user? <router-link to="/login">Sign In</router-link>
        </p>

      </div>

      <TextButton @clickEvent="createUser" :disabled="invalid"> {{buttonMsg}} </TextButton>

      <p class="text-error"> {{ errorMsg }} </p>
      <p class="text-center"> {{ successMsg }} </p>
    </ValidationObserver>
  </div>
</section>
</template>

<script>
import NavigationBar from "../components/NavigationBar.vue";
import SingleInput from "../components/SingleInput.vue";
import TextButton from "../components/TextButton.vue";

import {
  ValidationProvider,
  ValidationObserver,
  extend
} from 'vee-validate';

import {
  required,
  email,
  max,
  min,
} from 'vee-validate/dist/rules';

extend('required', {
  ...required,
  message: 'This field is required!'
});

extend('email', {
  ...email,
  message: 'Invalid E-Mail address!'
});

extend('max', {
  ...max,
  message: 'Must have at most {length} characters!'
});

extend('min', {
  ...min,
  message: 'Must have at least {length} characters!'
});

export default {
  name: "Register",
  components: {
    NavigationBar,
    TextButton,
    SingleInput,
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      form: {
        name: "",
        email: "",
        password: "",
      },
      errorMsg: "",
      buttonMsg: "REGISTER",
      successMsg: "",
    };
  },
  methods: {
    createUser() {
      this.$http
        .post('/users/register', this.form)
        .then(response => {
          console.log(response)
          this.buttonMsg = 'DONE!'
          this.successMsg = 'Success! Now you can Sign In!'
          setTimeout(() => {
            this.$router.push('/login')
          }, 3000)
        })
        .catch(error => {
          console.log(error.response)

          this.errorMsg = error.response.data.msg;
        });
    }
  }
};
</script>

<style scoped>
.register-flex {
  min-height: 90%;

  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-around;
}

.form-input {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.text-label {
  color: #626468;
  text-align: left;
}

.text-center {
  color: #626468;
  text-align: center;
}

.text-error {
  color: #FF7171;
}

.text-center a {
  text-decoration: none;
  color: #121213;
}

/* Refactor the same! */
.icon {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}

.text-label img {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}
</style>
