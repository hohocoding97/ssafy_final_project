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
        if (!username){
          window.alert('아이디를 입력해주세요')
        } else if (!password1){
          window.alert('비밀번호를 입력해주세요')
        } else if (!password2) {
          window.alert('비밀번호 확인란을 입력해주세요')
        } else if (password1 === password2){
          window.alert('이미 존재하는 아이디입니다.')
        } else {
          window.alert('비밀번호가 일치하지 않습니다.')
        }
      })
  }
  const token = ref('')
  const login = function(payload){
    const { username, password } = payload
    axios({
      method:'POST',
      url:`${API_URL}/accounts/login/`,
      data: {username, password},
    })
      .then((res) => {
        console.log('로그인 성공')
        console.log(res.data)
        token.value = res.data.key
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signup, token, login }
}, {persist: true})
