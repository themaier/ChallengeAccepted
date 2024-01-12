import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStore = defineStore('store', () => {
  const loggedIn = ref(localStorage.getItem('loggedIn') === 'true')
  const user = ref(JSON.parse(localStorage.getItem('user')))
  
  return { loggedIn, user }
})
