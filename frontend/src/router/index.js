import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignInView from '../views/SignInView.vue'
import SignUpView from '../views/SignUpView.vue'
import CreateChallengeView from '../views/CreateChallengeView.vue'
import TrendingView from '../views/TrendingView.vue'
import FriendsView from '../views/FriendsView.vue'
import CompletedChallengesView from '../views/CompletedChallengesView.vue'
import FriendsProfileView from '../views/FriendsProfileView.vue'

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
    {
      path: '/erstellen',
      name: 'create',
      component: CreateChallengeView
    },
    {
      path: '/freunde',
      name: 'friends',
      component: FriendsView
    },
    {
      path: '/trends',
      name: 'trending',
      component: TrendingView
    },
    {
      path: '/abgeschlossen',
      name: 'completed',
      component: CompletedChallengesView
    },
    {
      path: '/user/:username',
      name: 'friendProfile',
      component: FriendsProfileView
    }
  ]
})

export default router
