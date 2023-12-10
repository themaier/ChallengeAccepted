import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStore = defineStore('store', () => {
  const loggedIn = ref(true)
  return { loggedIn }
})
