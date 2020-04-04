<template>
<div class="options-item" v-bind:style="{ background: getGradientString(percentageCurrent) }">
  <slot></slot>
</div>
</template>

<script>
export default {
  name: 'ProgressBar',
  props: ['percentage'],

  data() {
    return {
      updateInterval: null,
      percentageCurrent: 0,
      randomHue: 0,
    };
  },
  methods: {
    getGradientString(percentage) {
      return 'linear-gradient(to right, hsl(' + this.randomHue + ', 73%, 77%), hsl(' + this.randomHue + ', 73%, 77%) ' + percentage + '%, #FFFFFF ' + percentage + '%, #FFFFFF)';
    },
    updateProgress(time) {
      clearInterval(this.updateInterval);

      this.updateInterval = setInterval(() => {
        if (this.percentageCurrent == this.percentage) {
          clearInterval(this.updateInterval);
        }

        if (this.percentageCurrent < this.percentage) {
          this.percentageCurrent = this.percentageCurrent + 1;
        } else if (this.percentageCurrent > this.percentage) {
          this.percentageCurrent = this.percentageCurrent - 1;
        }

      }, time)
    }
  },
  watch: {
    percentage: function() {
      this.updateProgress(50);
    }
  },
  created() {
    this.updateProgress(10);

    this.randomHue = Math.random() * 360;
  },
  beforeDestroy() {
    clearInterval(this.updateInterval);
  }
}
</script>

<style scoped>
:root {
  --color-primary-angle: 90deg;
}

.options-item {
  overflow-wrap: break-word;

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
</style>
