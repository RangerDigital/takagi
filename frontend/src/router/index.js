import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/navigation',
    name: 'Navigation',
    component: () => import('../views/Navigation.vue')
  },
  {
    path: '/create',
    name: 'PollsCreate',
    component: () => import('../views/PollsCreate.vue')
  },
  {
    path: '/polls',
    name: 'Polls',
    component: () => import('../views/Polls.vue')
  },
  {
    path: '/polls/:pollId/results',
    name: 'PollsResults',
    component: () => import('../views/PollsResults.vue')
  },
  {
    path: '/polls/:pollId',
    name: 'PollsVote',
    component: () => import('../views/PollsVote.vue')
  },
  {
    path: '*',
    name: 'Error404',
    component: () => import('../views/Error404.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
