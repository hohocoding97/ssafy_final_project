import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const movieCounterStore = defineStore('movieCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'
  const imgURL = 'https://image.tmdb.org/t/p/w200'

  const allMovies = ref(null) // 홈에서 사용될 영화 데이터
  const popularMovies = ref(null) // 인기 영화 데이터
  const latestMovies = ref(null) // 최신 영화 데이터
  
  const fetch_movies = function(){
    axios.get(`${API_URL}/movies/`)
    .then(res => allMovies.value = res.data)
    .catch(err => console.log('모든 영화 가져올때 에러 발생함',err))
    axios.get(`${API_URL}/movies/popular/`)
    .then(res => popularMovies.value = res.data)
    .catch(err => console.log('인기 영화 가져올때 에러 발생함', err))
    axios.get(`${API_URL}/movies/latest/`)
    .then(res => latestMovies.value = res.data)
    .catch(err => console.log(err))
  }

  return { API_URL,imgURL,allMovies, popularMovies, latestMovies, fetch_movies }
}, {persist:true})
