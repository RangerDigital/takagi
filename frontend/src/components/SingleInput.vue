<template>
<input :value="value" v-on:input="updateValue($event.target.value)" v-on:keyup.enter="clickEnter" class="input">
</template>


<script>
export default {
  name: "SingleInput",
  props: {
    value: {
      type: String
    }
  },
  methods: {
    updateValue: function(value) {
      this.$emit('input', value)
    },
    clickEnter: function() {
      this.$emit('onEnter')
    }
  }
};
</script>


<style scoped>
.input {
  width: 30rem;

  display: block;
  margin: 0 auto;

  background-color: #FFFFFF;

  border: 1.5px solid #121213;
  border-radius: 5px;

  margin-top: 0.5rem;
  margin-bottom: 1rem;

  font-family: 'Baloo Thambi 2';

  text-align: left;

  font-size: 1.6rem;
  font-weight: 500;
  letter-spacing: 0.1em;

  color: #121213;
  padding: 0.6em;
}

.input:focus {
  outline: none;
}

.input-error {
  border: 1.5px solid #FF7171;
}
</style>
