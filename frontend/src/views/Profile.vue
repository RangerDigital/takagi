<template>
  <section class="g-full-page">
    <NavigationBar title="My Profile" />

    <ValidationObserver v-slot="{ invalid }">
      <div class="g-component-flex">
        <div>
          <h1 class="heading-text">Welcome back, {{ form.name }}!</h1>
          <form>
            <div class="form-input">
              <ValidationProvider rules="required|min:3|max:15" v-slot="v">
                <label>
                  <p class="form-label"><img class="g-form-icon" src="../assets/icon-tag.svg" alt="Tag Icon" />Name</p>
                  <SingleInput v-model="form.name" placeholder="e.g. John" data-cy="profile-name" />
                </label>
                <p class="text-error" v-if="v.errors.length"><img class="g-form-icon" src="../assets/icon-alert-red.svg" alt="Alert Icon" /> {{ v.errors[0] }}</p>
                <p class="text-center" v-else>. . .</p>
              </ValidationProvider>
            </div>

            <div class="form-input">
              <ValidationProvider rules="required|email" v-slot="v">
                <label>
                  <p class="form-label"><img class="g-form-icon" src="../assets/icon-mail.svg" alt="E-Mail Icon" />E-Mail</p>
                  <SingleInput v-model="form.email" type="email" placeholder="e.g. me@gmail.com" data-cy="profile-email" />
                </label>
                <p class="text-error" v-if="v.errors.length"><img class="g-form-icon" src="../assets/icon-alert-red.svg" alt="Alert Icon" /> {{ v.errors[0] }}</p>
                <p class="text-center" v-else>. . .</p>
              </ValidationProvider>
            </div>
          </form>
        </div>

        <div>
          <h1 class="heading-text">Change Password</h1>
          <p class="text-center">Optional, only If you want to change it!</p>

          <div class="form-input">
            <ValidationProvider rules="min:8" v-slot="v">
              <label>
                <p class="form-label"><img class="g-form-icon" src="../assets/icon-lock.svg" alt="Lock Icon" />New Password</p>
                <SingleInput v-model="password" placeholder="e.g. Pretty obvious, right?" data-cy="profile-password" />
              </label>
              <p class="text-error" v-if="v.errors.length"><img class="g-form-icon" src="../assets/icon-alert-red.svg" alt="Alert Icon" /> {{ v.errors[0] }}</p>
              <p class="text-center" v-else>. . .</p>
            </ValidationProvider>
          </div>
        </div>

        <div>
          <TextButton @clickEvent="updateUser" :disabled="invalid">UPDATE</TextButton>
          <p class="text-error"> {{ serverErrorMsg }} </p>
          <p v-show="isSuccess" class="text-center">Success! Information updated!</p>
        </div>
      </div>
    </ValidationObserver>
  </section>
</template>

<script>
  import NavigationBar from "../components/NavigationBar.vue";
  import SingleInput from "../components/SingleInput.vue";
  import TextButton from "../components/TextButton.vue";

  import { ValidationProvider, ValidationObserver, extend } from "vee-validate";

  import { required, email, max, min } from "vee-validate/dist/rules";

  extend("required", {
    ...required,
    message: "This field is required!",
  });

  extend("email", {
    ...email,
    message: "Invalid E-Mail address!",
  });

  extend("max", {
    ...max,
    message: "Must have at most {length} characters!",
  });

  extend("min", {
    ...min,
    message: "Must have at least {length} characters!",
  });

  export default {
    name: "Profile",
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
        },

        password: "",

        isSuccess: false,
        serverErrorMsg: "",
      };
    },
    methods: {
      updateUser() {
        this.$http
          .patch("/api/users/me", this.form)
          .then(() => {
            this.isSuccess = true;
          })
          .catch((error) => {
            this.isSuccess = false;
            this.serverErrorMsg = error.response.data.msg;
          });

        if (this.password) {
          this.$http
            .post("/api/users/me/password", {
              password: this.password,
            })
            .then(() => {
              this.isSuccess = true;
            })
            .catch((error) => {
              this.isSuccess = false;
              this.serverErrorMsg = error.response.data.msg;
            });
        }
      },
    },
    created() {
      this.$http
        .get("/api/users/me")
        .then((response) => {
          this.form.name = response.data.name;
          this.form.email = response.data.email;
        })
        .catch((error) => {
          console.log(error);

          if (error.response.status === 401) {
            localStorage.removeItem("jwt_token");
            this.$http.defaults.headers.common["Authorization"] = "";

            this.$router.push("/");
          }
        });
    },
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

  .heading-text {
    margin-top: 0.3em;
    margin-bottom: 0.3em;

    font-size: 2.2rem;
    text-align: left;
    width: 30rem;
  }

  .text-center {
    color: #626468;
    text-align: center;
  }

  .text-error {
    color: #ff7171;
  }

  .text-link {
    color: #121213;
    text-decoration: none;
    transition: all 0.5s;
  }

  .text-link:hover {
    color: #ff7171;
  }
</style>
