import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignInView from '../views/SignInView.vue'
import SignUpView from '../views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/anmelden',
      name: 'signIn',
      component: SignInView
    },
    {
      path: '/registrieren',
      name: 'signUp',
      component: SignUpView
    },
  ]
})

export default router
