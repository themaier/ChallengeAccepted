import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useStore = defineStore('store', () => {
  const loggedIn = ref(localStorage.getItem('loggedIn') === 'true')
  const user = ref(JSON.parse(localStorage.getItem('user')))
  const isVideo = (resourcePath) => {
    const videoExtensions = ['mp4']; 
    const extension = resourcePath.toLowerCase().split('.').pop();
    console.log(extension)
    return videoExtensions.includes(extension);
  }

  return { loggedIn, user, isVideo }
})
