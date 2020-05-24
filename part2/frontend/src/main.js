import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap'
import '@/assets/css/style.css'
import Bootstrap4Vue from 'bootstrap4-vue'

Vue.use(Bootstrap4Vue);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
