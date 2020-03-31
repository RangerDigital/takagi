<template>
<section class="g-full-page">
  <NavigationBar title="Sign Up" />

  <ValidationObserver v-slot="{ invalid }">
    <div class="g-component-flex">
      <form>
        <div class="form-input">
          <p class="form-label"><img class="form-icon" src="../assets/icon-tag.svg">Name</p>
          <ValidationProvider rules="required|min:3|max:15" v-slot="v">
            <SingleInput v-model="form.name" placeholder="e.g. John" />
            <p class="text-error" v-if="v.errors.length"><img class="form-icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
            <p class="text-center" v-else>. . .</p>
          </ValidationProvider>
        </div>

        <div class="form-input">
          <p class="form-label"><img class="form-icon" src="../assets/icon-lock.svg">E-Mail</p>
          <ValidationProvider rules="required|email" v-slot="v">
            <SingleInput v-model="form.email" type="email" placeholder="e.g. me@gmail.com" />
            <p class="text-error" v-if="v.errors.length"><img class="form-icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
            <p class="text-center" v-else>. . .</p>
          </ValidationProvider>
        </div>

        <ValidationProvider class="form-input" rules="required|min:8" v-slot="v">
          <p class="form-label"><img class="form-icon" src="../assets/icon-mail.svg">Password</p>
          <SingleInput v-model.lazy="form.password" type="password" placeholder="e.g. Pretty obvious, right?" />
          <p class="text-error" v-if="v.errors.length"><img class="form-icon" src="../assets/icon-alert-red.svg"> {{ v.errors[0] }}</p>
          <p class="text-center" v-else>. . .</p>
        </ValidationProvider>

        <p class="text-center">
          Existing user? <a @click="$router.push('/login')" class="text-link g-clickable">Sign In</a>
        </p>
      </form>

      <div>
        <TextButton @clickEvent="createUser" :disabled="invalid">REGISTER</TextButton>
        <p class="text-error"> {{ serverErrorMsg }} </p>
        <p v-show="isSuccess" class="text-center">Success! Now you can Sign In!</p>
      </div>
    </div>
  </ValidationObserver>
</section>
</template>

<script>
import NavigationBar from '../components/NavigationBar.vue';
import SingleInput from '../components/SingleInput.vue';
import TextButton from '../components/TextButton.vue';

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
  name: 'Register',
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
        name: '',
        email: '',
        password: '',
      },

      isSuccess: false,
      serverErrorMsg: '',
    };
  },
  methods: {
    createUser() {
      if (this.isSuccess) {
        return;
      }

      this.$http
        .post('/api/users/register', this.form)
        .then(() => {
          this.isSuccess = true;

          setTimeout(() => {
            this.$router.push('/login')
          }, 1000)
        })
        .catch(error => {
          this.isSuccess = false;
          this.serverErrorMsg = error.response.data.msg;
        });
    }
  }
};
</script>

<style scoped>
.form-input {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.form-label {
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

.text-link {
  color: #121213;
  text-decoration: none;
  transition: all 0.5s;
}

.text-link:hover {
  color: #FF7171;
}

.form-icon {
  display: inline;

  height: 2.5rem;
  vertical-align: text-bottom;

  margin-right: 0.5rem;
}
</style>
