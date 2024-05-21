import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('useCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'
  const router = useRouter()
  const is_login = ref(false)
  const signup = function(payload) {
    const { username, password1, password2 } = payload
    axios({
      method:'POST',
      url: `${API_URL}/accounts/signup/`,
      data: {username, password1, password2}
    })
      .then((res)=>{
        console.log('회원가입성공')
        payload = {username, password : password1}
        login(payload)      //회원가입후 로그인까지하기
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
  const token = ref(null)
  const userInfo = ref({
    username: '',
    id: '',
    image_url : '',
    email : '',
    nick_name : '',
  })
  const login = function(payload){
    const { username, password } = payload
    axios({
      method:'POST',
      url:`${API_URL}/accounts/login/`,
      data: {username, password},
    })
      .then((res) => {
        console.log('로그인 성공')
        token.value = res.data.key
        is_login.value = true
        router.push({name:'home'})
        axios({
          method : 'GET',
          url:`${API_URL}/users/`,
          headers : {
            Authorization: `Token ${token.value}`
          }
        })
          .then(res => {
            console.log(res.data)
            userInfo.value.username = res.data.username
            userInfo.value.id = res.data.id
            userInfo.value.image_url = res.data.image_url
            userInfo.value.email = res.data.email
            userInfo.value.nick_name = res.data.nick_name
            console.log('내 정보 가져오기 성공')
          })
          .catch(err => console.log('내 정보 가져오기 실패', err))
      })
      .catch((err) => {
        console.log('로그인 실패',err)
      })
  }
  
  const logout = function(){
    axios({
      method:'POST',
      url:`${API_URL}/accounts/logout/`,
      headers: {Authorization: `Token ${token.value}`}
    })
    .then(res => {
      token.value = ''
      userInfo.value.username = ''
      userInfo.value.id = ''
      userInfo.value.image_url = ''
      userInfo.value.email = ''
      userInfo.value.nick_name = ''
      is_login.value = false
      console.log('로그아웃성공',res.data)
    })
    .catch(err => console.log('로그아웃실패',err))
  }

  return { API_URL, token,  userInfo, is_login, signup, login, logout}
}, {persist: true})
