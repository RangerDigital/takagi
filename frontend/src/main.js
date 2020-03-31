import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';

Vue.config.productionTip = false
Vue.prototype.$http = axios

Sentry.init({
  dsn: 'https://64b1d0177b2e4ea2845d71b77addafb2@sentry.io/5184010',
  integrations: [new Integrations.Vue({Vue, attachProps: true})],
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
