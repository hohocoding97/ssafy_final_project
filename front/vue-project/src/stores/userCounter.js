import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('useCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'
  const router = useRouter()
  const is_login = ref(false)
  const token = ref(null)
  const like_movies = ref(null)

  const userInfo = ref({
    username: '',
    id: '',
    image_url : '',
    email : '',
    nick_name : '',
    like_movies : [],
  })

  const profileInfo = ref({
    username: '',
    id: '',
    image_url : '',
    email : '',
    nick_name : '',
    like_movies : [],
  })

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
        getUserInfo()
      })
      .catch((err) => {
        console.log('로그인 실패',err)
      })
  }
  const getUserInfo = function() {
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
        userInfo.value.like_movies = res.data.like_movies
        console.log('내 정보 가져오기 성공')
      })
      .catch(err => console.log('내 정보 가져오기 실패', err))

    
  }
  
  const getProfileInfo = function(userId) {
    axios({
      method : 'GET',
      url:`${API_URL}/users/${userId}/`,
    })
      .then(res => {
        console.log(res.data)
        profileInfo.value.username = res.data.username
        profileInfo.value.id = res.data.id
        profileInfo.value.image_url = res.data.image_url
        profileInfo.value.email = res.data.email
        profileInfo.value.nick_name = res.data.nick_name
        profileInfo.value.like_movies = res.data.like_movies
        console.log('프로필 정보 가져오기 성공')
      })
      .catch(err => console.log('프로필 정보 가져오기 실패', err))

      axios.get(`${API_URL}/users/${userId}/like_movies/`)
      .then((res) => like_movies.value = res.data)
      .catch((err) => console.log(err))
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

  const follow = function() {
    if (!is_login){ window.alert('로그인이 필요합니다') }
    else if (userInfo.value.id === profileInfo.value.id) { window.alert('잘못된 접근입니다') }
    else { 
      axios({
        method : 'POST',
        url: `${API_URL}/users/${profileInfo.value.id}/follow/`,
        headers : { Authorization : `Token ${token.value}` }
      })
        .then((res) => console.log(res.data))
        .catch((err) => console.log(err))
    }
  }
  return { API_URL, token,  userInfo, is_login, profileInfo, like_movies,
    signup, login, logout, getUserInfo ,getProfileInfo, follow, }
}, {persist: true})
