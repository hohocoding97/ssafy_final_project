import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('useCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'

  const signup = function(payload) {
    const { username, password1, password2 } = payload
    axios({
      method:'POST',
      url: `${API_URL}/accounts/signup/`,
      data: {username, password1, password2}
    })
      .then((res)=>{
        console.log('회원가입성공')
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signup }
})
