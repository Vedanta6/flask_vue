import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import '@/assets/css/style.css'
import Bootstrap4Vue from 'bootstrap4-vue'
import vuetify from '@/plugins/vuetify'

Vue.use(Bootstrap4Vue);
Vue.config.productionTip = false

Vue.directive('blur', {
  inserted: function (el) {
    el.onfocus = (ev) => ev.target.blur()
  }
});

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
