import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ShoppingList from '../views/ShoppingList.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/shoppinglist',
      name: 'shoppingList',
      component: ShoppingList
    },
    {
      path: '*',
      redirect: '/'
    }
  ],
  linkActiveClass: 'active',
})
